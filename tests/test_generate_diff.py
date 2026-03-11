import os

import pytest

from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


@pytest.mark.parametrize('file_format', ['json', 'yml'])
def test_generate_diff(file_format):
    file1 = get_fixture_path(f'file1.{file_format}')
    file2 = get_fixture_path(f'file2.{file_format}')

    with open(get_fixture_path('expected_result.txt')) as f:
        expected = f.read().strip()

    assert generate_diff(file1, file2) == expected
