import pytest


@pytest.fixture
def data():
    return [1, 2, 3, 4]


def test_append(data):
    data.append(5)
    assert data == [1, 2, 3, 4, 5]


if __name__ == '__main__':
    pytest.main(['-v'])
