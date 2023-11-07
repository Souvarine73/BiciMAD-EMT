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
        emt_instance.select_valid_urls()
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

