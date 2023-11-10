import io
import re
import requests
import zipfile


class UrlEMT:
    """
    This class allow us to use the BiciMAD API and retrieve a csv file
    for a given mont and year
    """

    # Constants
    EMT = "https://opendata.emtmadrid.es"
    GENERAL = "/Datos-estaticos/Datos-generales-(1)"

    def __init__(self):
        """
        Constructor that updates the set of valid urls of BiciMAS API
        """
        self.urls = UrlEMT.select_valid_urls()

    @staticmethod
    def get_links(html) -> set:
        """
        It gets all the links from BiciMAD API that match the described reg exp
        :param html: html file. In this case BiciMAD API HTML
        :return: Set of urls from BiciMAD API
        """
        patron = r'/getattachment/[^"]+/trips_\d{2}_\d{2}_[A-Za-z]+-csv\.aspx'
        datare = re.compile(patron)
        matches = datare.findall(html)
        return set(matches)

    @staticmethod
    def select_valid_urls() -> set:
        """
        It returns only valids urls from BiciMAD API.
        :return: Set of valids urls from BiciMAD API
        """
        url = UrlEMT.EMT + UrlEMT.GENERAL
        response = requests.get(url)

        if response.status_code == 200:
            valid_urls = UrlEMT.get_links(response.text)
            return valid_urls
        else:
            raise ConnectionError("The connection was not successful")

    def get_url(self, month: int, year: int) -> str:
        """
        This method select a given url from the set of valid urls previously defined
        :param month: Month of the year used to select the right url
        :param year: Year used to select the right url
        :return: String with the desired url if exists
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
        for urls in self.urls:
            if url in urls:
                return UrlEMT.EMT + urls

        # if not found an error is raised
        raise ValueError("Month and year not found")

    def get_csv(self, month: int, year: int) -> io.StringIO:
        """
        This method creates a csv file
        :param month: Month of the year used to select the right url
        :param year: Year used to select the right url
        :return: io.String object containing a csv file
        """
        link = self.get_url(month, year)
        response = requests.get(link)

        if response.status_code != 200:
            raise ConnectionError("The connection was not successful")

        bytes_doc = io.BytesIO(response.content)
        with zipfile.ZipFile(bytes_doc) as zip:
            with zip.open(zip.namelist()[0]) as csvfile:
                return io.StringIO(csvfile.read().decode('utf-8'))
