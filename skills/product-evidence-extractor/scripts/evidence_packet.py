"""Create bounded documentary inputs and validate quote provenance, not meaning."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def page_numbers(spec, count):
    if not spec:
        return list(range(1, count + 1))
    numbers = set()
    for token in spec.split(','):
        endpoints = token.split('-')
        if len(endpoints) == 1:
            first = last = int(token)
        elif len(endpoints) == 2:
            first, last = map(int, endpoints)
        else:
            raise ValueError('Invalid page range')
        if not 1 <= first <= last <= count:
            raise ValueError('Page outside source document')
        numbers.update(range(first, last + 1))
    return sorted(numbers)


def prepare(sources, output, target, pages=None):
    output = Path(output).resolve()
    if output.exists():
        raise ValueError('Use an unused packet directory; do not overwrite evidence')
    staged = []
    for index, source in enumerate(sources):
        source = Path(source).resolve()
        before = digest(source)
        if source.suffix.lower() == '.pdf':
            text = subprocess.run(['pdftotext', '-layout', str(source), '-'],
                                  check=True, capture_output=True, text=True, timeout=120).stdout
            texts = text.split('\f')
            if texts and not texts[-1].strip():
                texts.pop()
        elif source.suffix.lower() in {'.txt', '.md'}:
            texts = [source.read_text()]
        else:
            raise ValueError('Supply PDF or UTF-8 .txt/.md source')
        if digest(source) != before:
            raise ValueError('Source changed during extraction')
        selected = page_numbers(pages, len(texts))
        staged.append((dict(source_id='source-' + str(index + 1), path=str(source),
                            sha256=before, page_count=len(texts), pages=[]), texts, selected))
    if not staged:
        raise ValueError('At least one source required')
    output.mkdir(parents=True)
    manifest = {'schema': 'product-source-packet/1', 'target': target, 'sources': []}
    for row, texts, selected in staged:
        for page in selected:
            path = output / (row['source_id'] + '-page-' + str(page) + '.txt')
            path.write_text(texts[page - 1])
            row['pages'].append(dict(page=page, text=path.name, sha256=digest(path),
                                     needs_visual_review=not bool(texts[page - 1].strip())))
        manifest['sources'].append(row)
    (output / 'sources.json').write_text(json.dumps(manifest, indent=2) + '\n')
    return manifest


def validate(packet, claims):
    packet = Path(packet).resolve()
    manifest = json.loads((packet / 'sources.json').read_text())
    if manifest.get('schema') != 'product-source-packet/1':
        raise ValueError('Unknown source packet schema')
    if claims.get('schema') != 'product-evidence/1' or claims.get('target') != manifest['target']:
        raise ValueError('Evidence target/schema differs from source packet')
    if not isinstance(claims.get('claims'), list) or not isinstance(claims.get('unresolved'), list):
        raise ValueError('Provide claims and unresolved lists')
    if not claims['claims'] and not claims['unresolved']:
        raise ValueError('Empty evidence result')
    pages = {}
    for source in manifest['sources']:
        if digest(source['path']) != source['sha256']:
            raise ValueError('Source changed: ' + source['source_id'])
        for page in source['pages']:
            path = (packet / page['text']).resolve()
            if not path.is_relative_to(packet) or digest(path) != page['sha256']:
                raise ValueError('Extracted page changed')
            pages[(source['source_id'], page['page'])] = ' '.join(path.read_text().split())
    for claim in claims['claims']:
        if not all(key in claim for key in ('field', 'value', 'unit', 'applicability', 'citations')):
            raise ValueError('Incomplete claim')
        if not isinstance(claim['field'], str) or not claim['field'].strip() or claim['value'] is None:
            raise ValueError('Empty claim field/value')
        if claim['applicability'] not in {'exact-variant', 'family'}:
            raise ValueError('Unknown variant applicability')
        if not isinstance(claim['citations'], list) or not claim['citations']:
            raise ValueError('Claim requires citations')
        for cite in claim['citations']:
            quote = ' '.join(cite['quote'].split())
            if not quote or quote not in pages.get((cite['source_id'], cite['page']), ''):
                raise ValueError('Quote not found on cited page: ' + claim['field'])
    return {'status': 'provenance-validated', 'claims': len(claims['claims']),
            'unresolved': len(claims['unresolved']), 'semantic_review_required': True}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    p = commands.add_parser('prepare')
    p.add_argument('--source', action='append', required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--pages')
    for name in ('manufacturer', 'model', 'variant'):
        p.add_argument('--' + name, required=True)
    p = commands.add_parser('validate')
    p.add_argument('--packet', type=Path, required=True)
    p.add_argument('--claims', type=Path, required=True)
    args = parser.parse_args()
    if args.command == 'prepare':
        result = prepare(args.source, args.output, {k: getattr(args, k) for k in ('manufacturer', 'model', 'variant')}, args.pages)
    else:
        result = validate(args.packet, json.loads(args.claims.read_text()))
    print(json.dumps(result, indent=2))
