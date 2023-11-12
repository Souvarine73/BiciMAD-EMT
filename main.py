from bicimad.UrlEMT import UrlEMT
from bicimad.BiciMad import BiciMad
import requests
import io

if __name__ == "__main__":
    EMT = "https://opendata.emtmadrid.es"
    GENERAL = "/Datos-estaticos/Datos-generales-(1)--???"
    a = BiciMad(2, 23)
    a.clean()
    b = a._data
    c = b.shape
    print(c[1])
