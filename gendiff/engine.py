import os

from gendiff.formatters.stylish import format_stylish
from gendiff.parser import parse


def get_data(file_path):
    _, extension = os.path.splitext(file_path)
    format = extension[1:]
    with open(file_path, 'r') as f:
        content = f.read()
    return parse(content, format)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    diff = build_diff(data1, data2)

    return format_stylish(diff)


def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    result = []

    for key in keys:
        if key not in data1:
            result.append({
                'key': key, 'status': 'added', 'value': data2[key]
            })
        elif key not in data2:
            result.append({
                'key': key, 'status': 'deleted', 'value': data1[key]
            })
        elif data1[key] == data2[key]:
            result.append({
                'key': key, 'status': 'unchanged', 'value': data1[key]
            })
        else:
            result.append({
                'key': key,
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })
    return result
