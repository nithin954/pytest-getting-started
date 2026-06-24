import pytest


@pytest.mark.math
def test_m1():
    a = 3
    b = 5
    assert a + 2 == b


@pytest.mark.math
def test_m2():
    a = 1
    b = 2
    assert a + 1 != b, "test failed because a is not equal to b"


@pytest.mark.str
def test_m3():
    assert False


@pytest.mark.str
def test_m4():
    assert "naveen".upper() == "NAVEEN", "'naveen' is not equal to 'NAVEEN'"
