import pandas as pd

from bicimad.UrlEMT import UrlEMT
from bicimad.BiciMad import BiciMad
import requests
import io
import datetime
import numpy as np

if __name__ == "__main__":
    EMT = "https://opendata.emtmadrid.es"
    GENERAL = "/Datos-estaticos/Datos-generales-(1)--???"
    a = BiciMad(2, 22)
    a.clean()
    var = a.station_unlock()
    print(len(var))
