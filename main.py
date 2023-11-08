from bicimad.UrlEMT import UrlEMT
from bicimad.BiciMad import BiciMad

if __name__ == "__main__":
    BiciMad1 = BiciMad(1, 23)
    b = BiciMad1.data
    print(b.info())
    BiciMad1.clean()
    a = BiciMad1.data
    print(a.info())
    print(a.head())

