import requests
import re


class UrlEMT:
    # Constants
    EMT = "https://opendata.emtmadrid.es"
    GENERAL = "/Datos-estaticos/Datos-generales-(1)"

    def __init__(self):
        self.set_valid_urls = set()

    @staticmethod
    def get_links(html) -> set:
        patron = r'href="/getattachment/[^"]+/trips_\d{2}_\d{2}_[A-Za-z]+-csv\.aspx"'
        datare = re.compile(patron)
        matches = datare.findall(html)
        return set(matches)

    def select_valid_urls(self):
        url = self.EMT + self.GENERAL
        response = requests.get(url)

        if response.status_code == 200:
            valid_urls = self.get_links(response.text)
            self.set_valid_urls = valid_urls
        else:
            raise ConnectionError("The connection was not successful")
