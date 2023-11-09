import pandas as pd
from .UrlEMT import UrlEMT


class BiciMad:

    def __init__(self, month: int, year: int):
        self._month = month
        self._year = year
        self._data = BiciMad.get_data(month, year)

    @staticmethod
    def get_data(month: int, year: int) -> pd.DataFrame:
        emt_instance = UrlEMT()
        emt_csv = emt_instance.get_csv(month, year)
        columns = ['idBike',
                   'fleet',
                   'trip_minutes',
                   'geolocation_unlock',
                   'address_unlock',
                   'unlock_date',
                   'locktype',
                   'unlocktype',
                   'geolocation_lock',
                   'address_lock',
                   'lock_date',
                   'station_unlock',
                   'unlock_station_name',
                   'station_lock',
                   'lock_station_name']

        df_initial = pd.read_csv(emt_csv, sep=';', index_col='fecha', parse_dates=['fecha', 'unlock_date', 'lock_date'])
        return df_initial[columns]

    @property
    def data(self):
        return self._data

    def __str__(self):
        return str(self._data)

    def clean(self):
        """

        :return:
        """
        # Delete rows filled with NaNs
        self._data.dropna(how='all', inplace=True)

        # Change data type form some columns
        columns_dict = {
            'fleet': 'string',
            'idBike': 'string',
            'station_lock': 'string',
            'station_unlock': 'string'
        }

        self._data = self._data.astype(columns_dict)

        # Remove the '.0' from the resultant conversion
        columns_list = ['fleet', 'idBike', 'station_lock', 'station_unlock']
        self._data[columns_list] = self._data[columns_list].apply(lambda x: x.str.rstrip('.0'))

    def resume(self) -> pd.Series:
        """

        :return:
        """
        year = self._year
        month = self._month
        usos_mes = len(self._data)
        total_hours = round(self._data['trip_minutes'].sum() / 60, 2)

        # Stations with most unblocks
        stations_unblocked = self._data.groupby('unlock_station_name').size()
        max_unblocked = stations_unblocked.max()
        stations = set(stations_unblocked[stations_unblocked == max_unblocked].index)

        data = {
            'year': year,
            'month': month,
            'total_uses': usos_mes,
            'total_time': total_hours,
            'most_popular_station': stations,
            'uses_from_most_popular': max_unblocked
        }

        data_series = pd.Series(data)

        return data_series
