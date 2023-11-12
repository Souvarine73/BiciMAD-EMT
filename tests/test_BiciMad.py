import pytest
from bicimad import BiciMad


@pytest.fixture
def create_bicimad():
    def _create_bicimad(month, year):
        return BiciMad(month, year)

    return _create_bicimad


@pytest.mark.parametrize("month, year", [(1, 23), (1, 22), (5, 22)])
def test_init(create_bicimad, month, year):
    b1 = create_bicimad(month, year)
    assert b1._month == month
    assert b1._year == year


def test_init_df():
    bici_object = BiciMad(2, 23)
    bici_object.clean()
    shape_values = bici_object._data.shape
    assert shape_values[0] == 168494
    assert shape_values[1] == 15
