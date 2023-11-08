import pandas as pd
from .UrlEMT import UrlEMT


class BiciMad:

    def __init__(self, month: int, year: int):
        self.__month = month
        self.__year = year
        self.__data = BiciMad.get_data(month, year)

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
        return self.__data

    def __str__(self):
        return str(self.__data)

    def clean(self):
        """

        :return:
        """
        # Delete rows filled with NaNs
        self.__data.dropna(how='all', inplace=True)

        # Change data type form some columns
        columns_dict = {
            'fleet': 'string',
            'idBike': 'string',
            'station_lock': 'string',
            'station_unlock': 'string'
        }

        self.__data = self.__data.astype(columns_dict)

        # Remove the '.0' from the resultant conversion
        columns_list = ['fleet', 'idBike', 'station_lock', 'station_unlock']
        self.__data[columns_list] = self.__data[columns_list].apply(lambda x: x.str.rstrip('.0'))


