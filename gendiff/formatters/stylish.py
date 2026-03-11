def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)


def format_stylish(diff):
    lines = ['{']

    for key, details in diff.items():
        status = details['status']

        if status == 'added':
            val = to_str(details['value'])
            lines.append(f"  + {key}: {val}")
        elif status == 'removed':
            val = to_str(details['value'])
            lines.append(f"  - {key}: {val}")
        elif status == 'unchanged':
            val = to_str(details['value'])
            lines.append(f"    {key}: {val}")
        elif status == 'changed':
            old_val = to_str(details['old_value'])
            new_val = to_str(details['new_value'])
            lines.append(f"  - {key}: {old_val}")
            lines.append(f"  + {key}: {new_val}")

    lines.append('}')
    return '\n'.join(lines)
