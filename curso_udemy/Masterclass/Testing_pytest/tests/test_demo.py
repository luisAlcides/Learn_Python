import pytest

from curso_udemy.Masterclass.Testing_pytest.app.demo import add, sub, div, discount_season


@pytest.mark.skip('Skipping the test for some reason')
def test_add():
    assert add(10, 20) == 30


@pytest.mark.skipif(discount_season, reason='skipping because discount season is on')
def test_sub():
    assert sub(20, 10) == 10


def test_div():
    assert div(100, 20) == 5

    # Case for asserting exception
    with pytest.raises(ZeroDivisionError):
        div(4, 0)
