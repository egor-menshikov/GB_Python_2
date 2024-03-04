import pytest


def test_func():
    assert 2 + 2 == 4, 'неверно'


if __name__ == '__main__':
    pytest.main(['-v'])
