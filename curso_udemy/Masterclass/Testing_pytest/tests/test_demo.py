import pytest

from curso_udemy.Masterclass.Testing_pytest.app.demo import add, sub, div


def test_add():
    assert add(10, 20) == 30


def test_sub():
    assert sub(20, 10) == 10


def test_div():
    assert div(100, 20) == 5

    #Case for asserting exception
    with pytest.raises(ZeroDivisionError):
        div(4, 0)