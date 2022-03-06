import pytest

status = 1

def test_sample1():
    assert status == 1


def test_sample2():
    assert status == 2


@pytest.mark.xfail()
def test_sample3():
    assert status == 1


@pytest.mark.xfail()
def test_sample4():
    assert status == 2

def test_sample5():
    assert status == 1