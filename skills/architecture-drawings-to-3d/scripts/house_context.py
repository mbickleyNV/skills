"""Return bounded context/impact from architecture-assembly/1 house XML."""
import argparse
from pathlib import Path
import xml.etree.ElementTree as ET


def context(path, target):
    path = Path(path).resolve()
    root = ET.parse(path).getroot()
    if root.get('schema') != 'architecture-assembly/1':
        raise ValueError('Expected architecture-assembly/1 schema')
    alias = root.find(f"./aliases/alias[@name='{target}']") if "'" not in target else None
    if alias is not None:
        target = alias.get('target')
    room_id, _, feature = target.partition(':')
    rooms = {r.get('id'): r for r in root.findall('./rooms/room')}
    if room_id not in rooms:
        raise ValueError('Unknown room or alias: ' + target)
    room = rooms[room_id]
    out = ET.Element('bounded-design-context', {'target': target, 'house': str(path)})
    for key in ['record', 'mesh', 'preview']:
        if room.get(key):
            ET.SubElement(out, 'file', {'role': key, 'path': str((path.parent / room.get(key)).resolve())})
    record_path = (path.parent / room.get('record')).resolve() if room.get('record') else None
    if record_path and record_path.exists():
        record = ET.parse(record_path).getroot()
        if feature:
            for node in record.iter():
                if node.get('id') == feature:
                    selected = ET.SubElement(out, 'selected-feature')
                    selected.append(ET.fromstring(ET.tostring(node)))
                    if node.get('image'):
                        ET.SubElement(out, 'file', role='source-crop', path=str((record_path.parent / node.get('image')).resolve()))
                    break
    for dependency in room.findall('dependency'):
        out.append(ET.fromstring(ET.tostring(dependency)))
    placement = room.find('placement')
    if placement is not None:
        out.append(ET.fromstring(ET.tostring(placement)))
    for interface in root.findall('./interfaces/interface'):
        if room_id in interface.get('rooms', '').split():
            out.append(ET.fromstring(ET.tostring(interface)))
    impact = ET.SubElement(out, 'impact')
    mode = 'placement-only' if feature in ['placement', 'transform'] else 'room-local'
    impact.set('mode', mode)
    if mode == 'room-local':
        ET.SubElement(impact, 'rebuild-room', {'id': room_id})
    if mode == 'room-local' and record_path:
        for candidate in rooms.values():
            if candidate.get('id') == room_id:
                continue
            matches = [d for d in candidate.findall('dependency')
                       if (path.parent / d.get('path')).resolve() == record_path
                       and (not feature or d.get('select') == "./parameters/parameter[@id='" + feature + "']")]
            if matches:
                downstream = ET.SubElement(impact, 'rebuild-room' if feature else 'conditional-rebuild-room', id=candidate.get('id'))
                for dependency in matches:
                    ET.SubElement(downstream, 'when-changed', select=dependency.get('select'))
    ET.SubElement(impact, 'recompose', {'artifact': 'assembly.3mf'})
    ET.SubElement(impact, 'refresh', {'artifact': 'assembly-preview.png review.html'})
    if feature.startswith('wall') or feature.startswith('room_'):
        ET.SubElement(impact, 'review-interfaces').text = 'Check listed shared interfaces before changing room envelope.'
    ET.indent(out)
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('house', type=Path)
    p.add_argument('target', help='room ID, room:feature, or declared alias')
    a = p.parse_args()
    try:
        out = context(a.house, a.target)
    except (ValueError, OSError, ET.ParseError) as e:
        p.exit(2, str(e) + '\n')
    print(ET.tostring(out, encoding='unicode'))


if __name__ == '__main__':
    main()
