import os

from gendiff.formatters import get_formatter
from gendiff.parser import parse


def get_data(file_path):
    _, extension = os.path.splitext(file_path)
    file_format = extension[1:]
    with open(file_path, 'r') as f:
        content = f.read()
    return parse(content, file_format)


def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    result = {}

    for key in keys:
        if key not in data1:
            result[key] = {'status': 'added', 'value': data2[key]}
        elif key not in data2:
            result[key] = {'status': 'removed', 'value': data1[key]}
        elif data1[key] == data2[key]:
            result[key] = {'status': 'unchanged', 'value': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {
                'status': 'nested',
                'value': build_diff(data1[key], data2[key])
            }
        else:
            result[key] = {
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            }
    return result


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    diff = build_diff(data1, data2)

    formatter = get_formatter(format_name)
    return formatter(diff)
