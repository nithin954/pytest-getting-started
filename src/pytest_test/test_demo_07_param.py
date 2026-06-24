import pytest


@pytest.mark.parametrize("value, result", [(1, 2), (2, 4), (3, 6)])
def test_calculation(value, result):
    assert value * 2 == result


@pytest.mark.parametrize("num, result", [(1, 1), (2, 4), (3, 9)])
def test_square(num, result):
    assert num**2 == result
