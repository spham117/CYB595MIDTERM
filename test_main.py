

from main import add, subtract, multiply, divide


def test_add():
    assert add(5, 4) == 9


def test_subtract():
    assert subtract(2, 3) == -1


def test_multiply():
    assert multiply(2, 5) == 10


def test_divide():
    assert divide(4, 2) == 2
