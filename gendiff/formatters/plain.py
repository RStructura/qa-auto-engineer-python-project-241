def to_str(value):
    if isinstance(value, dict) or isinstance(value, list):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff):
    def walk(node, path=""):
        lines = []
        for key, details in node.items():
            current_path = f"{path}.{key}" if path else key
            status = details['status']

            if status == 'nested':
                lines.append(walk(details['value'], current_path))
            elif status == 'added':
                value = to_str(details['value'])
                msg = f"Property '{current_path}' was added with value: {value}"
                lines.append(msg)
            elif status == 'removed':
                lines.append(f"Property '{current_path}' was removed")
            elif status == 'changed':
                old_val = to_str(details['old_value'])
                new_val = to_str(details['new_value'])
                msg = (f"Property '{current_path}' was updated. "
                       f"From {old_val} to {new_val}")
                lines.append(msg)
        return "\n".join(lines)

    return walk(diff)
