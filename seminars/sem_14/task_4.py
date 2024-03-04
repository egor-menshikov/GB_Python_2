import pytest
from task_1 import func


def test_one():
    assert func('hello world') == 'hello world'


def test_two():
    assert func('HELlO wOrLd') == 'hello world', 'ERROR'


def test_three():
    assert func('hello, wo,r!ld') == 'hello world'


def test_four():
    assert func('hELlыo, wo,r!ацацld') == 'hello world'


if __name__ == '__main__':
    pytest.main(['-v'])
