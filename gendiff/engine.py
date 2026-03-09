import json
import os

import yaml


def get_data(file_path):
    _, extension = os.path.splitext(file_path)

    with open(file_path, 'r') as f:
        if extension == '.json':
            return json.load(f)
        elif extension in ('.yml', '.yaml'):
            return yaml.safe_load(f)
    return None


def generate_diff(file_path1, file_path2):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    result = ['{']

    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                result.append(f'    {key}: {data1[key]}')
            else:
                result.append(f'  - {key}: {data1[key]}')
                result.append(f'  + {key}: {data2[key]}')
        elif key in data1:
            result.append(f'  - {key}: {data1[key]}')
        else:
            result.append(f'  + {key}: {data2[key]}')

    result.append('}')
    return '\n'.join(result)
