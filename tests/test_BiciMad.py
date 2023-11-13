import pandas as pd
import pytest
from bicimad import BiciMad
import numpy as np
import math


@pytest.fixture
def create_bicimad():
    def _create_bicimad(month, year):
        return BiciMad(month, year)

    return _create_bicimad


@pytest.fixture
def mock_bicimad() -> BiciMad:
    return BiciMad(2, 23)


@pytest.mark.parametrize("month, year", [(1, 23), (1, 22), (5, 22)])
def test_init(create_bicimad, month, year):
    b1 = create_bicimad(month, year)
    assert b1.__dict__['_month'] == month
    assert b1.__dict__['_year'] == year


def test_init_df(mock_bicimad):
    mock_bicimad.clean()
    shape_values = mock_bicimad.__dict__['_data'].shape
    assert shape_values[0] == 168494
    assert shape_values[1] == 15


def test_get_data():
    df = BiciMad.get_data(2, 23)
    columns_df = set(df.columns)
    columns_expected = {'idBike', 'fleet', 'trip_minutes', 'geolocation_unlock',
                        'address_unlock', 'unlock_date', 'locktype', 'unlocktype',
                        'geolocation_lock', 'address_lock', 'lock_date', 'station_unlock',
                        'unlock_station_name', 'station_lock', 'lock_station_name'}
    assert columns_df == columns_expected
    assert isinstance(df.index, pd.DatetimeIndex) \
           and np.issubdtype(df.unlock_date, np.datetime64) \
           and np.issubdtype(df.lock_date, np.datetime64)


def test_data():
    assert isinstance(BiciMad.get_data(2, 23), pd.DataFrame)


def test_clean(mock_bicimad):
    mock_bicimad.clean()
    assert ~mock_bicimad.data.isna().all(axis=1).any()
    coluns_string = ['fleet', 'idBike', 'station_lock', 'station_unlock']
    for column in coluns_string:
        assert pd.api.types.is_string_dtype(mock_bicimad.data[column])


def test_resume(mock_bicimad):
    data_expected = {'year': 23,
                     'month': 2,
                     'total_uses': 336988,
                     'total_time': 53890.1,
                     'most_popular_station': {'39 - Plaza de la Cebada'},
                     'uses_from_most_popular': 2189}
    result_expected = pd.Series(data_expected)
    result_obtained = mock_bicimad.resume()
    assert result_expected.equals(result_obtained)


@pytest.mark.parametrize("month, year, result", [(2, 23, 168), (1, 23, 312), (7, 22, 638)])
def test_num_station_non_blocked(create_bicimad, month, year, result):
    b1 = BiciMad(month, year)
    assert b1.num_station_non_blocked() == result


def test_df_fleet_1(mock_bicimad):
    assert len(mock_bicimad.data) == 336988
    mock_bicimad.clean()
    assert len(mock_bicimad.data) == 168494


def test_day_time(mock_bicimad):
    mock_bicimad.clean()
    assert math.isclose(mock_bicimad.day_time().max(), 4160.54)
    assert math.isclose(mock_bicimad.day_time().min(), 162.93)


@pytest.mark.parametrize("month, year, max, imax, min, imin",
                         [
                             (2, 23, 10349.66, 'X', 5626.44, 'M'),
                             (1, 22, 21988.31, 'L', 14638.71, 'D')
                         ])
def test_week_day_time(create_bicimad, month, year, max, imax, min, imin):
    b1 = BiciMad(month, year)
    b1.clean()
    b1_serie = b1.weekday_time()
    assert math.isclose(b1_serie.max(), max)
    assert math.isclose(b1_serie.min(), min)
    assert b1_serie.idxmax() == imax
    assert b1_serie.idxmin() == imin


@pytest.mark.parametrize("month, year, long",
                         [
                             (1, 22, 31),
                             (2, 22, 28),
                             (7, 22, 31)
                         ])
def test_total_usage_day(create_bicimad, month, year, long):
    b1 = BiciMad(month, year)
    b1.clean()
    b1_serie = b1.total_usage_day()
    assert len(b1_serie) == long


@pytest.mark.parametrize("month, year, long",
                         [
                             (1, 22, 7362),
                             (2, 22, 6697),
                             (7, 22, 7295)
                         ])
def test_station_unlock(create_bicimad, month, year, long):
    b1 = BiciMad(month, year)
    b1.clean()
    b1_serie = b1.station_unlock()
    assert len(b1_serie) == long
