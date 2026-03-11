def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def format_stylish(diff):
    lines = ['{']
    for item in diff:
        status = item['status']
        key = item['key']

        if status == 'added':
            lines.append(f'  + {key}: {to_str(item["value"])}')
        elif status == 'deleted':
            lines.append(f'  - {key}: {to_str(item["value"])}')
        elif status == 'unchanged':
            lines.append(f'    {key}: {to_str(item["value"])}')
        elif status == 'changed':
            lines.append(f'  - {key}: {to_str(item["old_value"])}')
            lines.append(f'  + {key}: {to_str(item["new_value"])}')

    lines.append('}')
    return '\n'.join(lines)
