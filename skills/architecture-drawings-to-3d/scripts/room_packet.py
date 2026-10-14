"""Extract a compact room packet from remodel-inference XML; standard library only."""
import argparse
import copy
import hashlib
from pathlib import Path
import sys
import xml.etree.ElementTree as ET


def extract(path, room_id, extra_regions=()):
    path = Path(path).resolve()
    root = ET.parse(path).getroot()
    if root.tag != 'remodel-inference':
        raise ValueError('Expected remodel-inference XML; adapt other schemas explicitly')
    rooms = {e.get('id'): e for e in root.findall('./rooms/room')}
    if room_id not in rooms:
        raise ValueError(f'Unknown room: {room_id}')
    room = rooms[room_id]
    out = ET.Element('room-packet', {
        'room': room_id, 'source': str(path),
        'source-sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
    })
    policy = root.find('interpretation-policy')
    if policy is not None:
        out.append(copy.deepcopy(policy))
    out.append(copy.deepcopy(room))
    refs = set(extra_regions)
    pages = {room.get('plan-page')} - {None}
    views = ET.SubElement(out, 'elevations')
    wanted = set(room.get('elevations', '').split())
    found_views = set()
    for e in root.findall('./interior-elevations/elevation'):
        if e.get('id') in wanted or room_id in e.get('rooms', '').split():
            views.append(copy.deepcopy(e))
            found_views.add(e.get('id'))
            refs.update(e.get('evidence', '').split())
            if e.get('page'):
                pages.add(e.get('page'))
    missing = [f'elevation:{v}' for v in sorted(wanted - found_views)]
    for collection, tag in [('components', 'component'), ('elements', 'element'),
                            ('relationships', 'relation'), ('corrections', 'correction')]:
        selected = [e for e in root.findall(f'./{collection}/{tag}')
                    if e.get('room') == room_id]
        if selected:
            dest = ET.SubElement(out, collection)
            for e in selected:
                dest.append(copy.deepcopy(e))
                refs.update(e.get('evidence', '').split())
    regions = {e.get('id'): e for e in root.findall('./evidence-regions/region')}
    sheets = {e.get('id'): e for e in root.findall('./sheets/sheet')}
    dest = ET.SubElement(out, 'evidence-regions')
    images = []
    for ref in sorted(refs):
        if ref in regions:
            e = copy.deepcopy(regions[ref])
            if e.get('image'):
                image = (path.parent / e.get('image')).resolve()
                e.set('image', str(image))
                images.append(str(image))
                if not image.is_file():
                    missing.append(f'image:{image}')
            dest.append(e)
            if e.get('page'):
                pages.add(e.get('page'))
        elif ref in sheets:
            pages.add(ref)
        else:
            missing.append(f'evidence:{ref}')
    dest = ET.SubElement(out, 'sheets')
    for page in sorted(pages):
        if page not in sheets:
            missing.append(f'sheet:{page}')
            continue
        e = copy.deepcopy(sheets[page])
        if e.get('image'):
            e.set('image', str((path.parent / e.get('image')).resolve()))
        dest.append(e)
    for value in missing:
        ET.SubElement(out, 'unresolved-reference').text = value
    ET.indent(out)
    return out, images, missing


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('xml', type=Path)
    parser.add_argument('room')
    parser.add_argument('--region', action='append', default=[])
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() == args.xml.resolve():
        parser.error('Output must not overwrite the source XML')
    try:
        out, images, missing = extract(args.xml, args.room, args.region)
    except (ValueError, ET.ParseError, OSError) as exc:
        parser.exit(2, f'{exc}\n')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(out).write(args.output, encoding='utf-8', xml_declaration=True)
    print(f'Packet: {args.output.resolve()}')
    for path in images:
        print(f'Image: {path}')
    for value in missing:
        print(f'Unresolved: {value}', file=sys.stderr)
    return 1 if missing else 0


if __name__ == '__main__':
    raise SystemExit(main())
