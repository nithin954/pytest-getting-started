def test_m1():
    a = 3
    b = 5
    assert a + b == 8, "test passed"


def test_m2():
    a = 1
    b = 2
    assert a + 1 != b, "test failed because a is not equal to b"


def test_m3():
    assert False


def test_m4():
    assert "naveen" == "NAVEEN", "'naveen' is not equal to 'NAVEEN'"
