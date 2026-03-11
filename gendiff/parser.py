import json

import yaml


def parse(data, format):
    if format == 'json':
        return json.loads(data)
    if format in ('yml', 'yaml'):
        return yaml.safe_load(data)
    raise ValueError(f'Unknown format: {format}')
