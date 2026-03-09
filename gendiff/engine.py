import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

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
