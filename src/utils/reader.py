from typing import List, Dict, Union


def read_employees(filepath: str) -> List[Dict[str, Union[str, int]]]:
    with open(filepath, encoding='utf-8') as f:
        lines = f.read().splitlines()

    header = lines[0].split(',')
    field_map = {
        'name': None,
        'department': None,
        'hours': None,
        'rate': None
    }

    for i, col in enumerate(header):
        lc = col.strip().lower()
        if lc == 'name':
            field_map['name'] = i
        elif lc == 'department':
            field_map['department'] = i
        elif lc in ('hourly_rate', 'rate', 'salary'):
            field_map['rate'] = i
        elif lc == 'hours_worked':
            field_map['hours'] = i

    result: List[Dict[str, Union[str, int]]] = []
    for line in lines[1:]:
        parts = line.split(',')
        result.append({
            'name': parts[field_map['name']].strip(),
            'department': parts[field_map['department']].strip(),
            'hours': int(parts[field_map['hours']]),
            'rate': int(parts[field_map['rate']])
        })
    return result