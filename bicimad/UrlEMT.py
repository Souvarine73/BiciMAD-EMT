import io
import re
import requests
import zipfile


class UrlEMT:
    # Constants
    EMT = "https://opendata.emtmadrid.es"
    GENERAL = "/Datos-estaticos/Datos-generales-(1)"

    def __init__(self):
        self.set_valid_urls = set()

    @staticmethod
    def get_links(html) -> set:
        """

        :param html:
        :return:
        """
        patron = r'/getattachment/[^"]+/trips_\d{2}_\d{2}_[A-Za-z]+-csv\.aspx'
        datare = re.compile(patron)
        matches = datare.findall(html)
        return set(matches)

    def select_valid_urls(self):
        """

        :return:
        """
        url = self.EMT + self.GENERAL
        response = requests.get(url)

        if response.status_code == 200:
            valid_urls = self.get_links(response.text)
            self.set_valid_urls = valid_urls
        else:
            raise ConnectionError("The connection was not successful")

    def get_url(self, month: int, year: int) -> str:
        """

        :param month:
        :param year:
        :return:
        """

        # If not in the selected range an error is raised
        if month < 1 or month > 12 or year < 21 or year > 23:
            raise ValueError("The month must be between 1 and 12 and the year between 21 and 23")

        # Fill with zeros the month and year
        month_str = str(month).zfill(2)
        year_str = str(year).zfill(2)

        # Creates de url to be checked in the set
        url = f"trips_{year_str}_{month_str}"

        # check if the selected url is in the set
        for urls in self.set_valid_urls:
            if url in urls:
                return self.EMT + urls

        # if not found an error is raised
        raise ValueError("Month and year not found")

    def get_csv(self, month: int, year: int) -> io.StringIO:
        """

        :param month:
        :param year:
        :return:
        """
        link = self.get_url(month, year)
        response = requests.get(link)

        if response.status_code != 200:
            raise ConnectionError("The connection was not successful")

        bytes_doc = io.BytesIO(response.content)
        with zipfile.ZipFile(bytes_doc) as zip:
            with zip.open(zip.namelist()[0]) as csvfile:
                return io.StringIO(csvfile.read().decode('utf-8'))