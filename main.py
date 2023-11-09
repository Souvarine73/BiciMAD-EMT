from bicimad.UrlEMT import UrlEMT
from bicimad.BiciMad import BiciMad

if __name__ == "__main__":
    BiciMad1 = BiciMad(2, 23)
    BiciMad1.clean()
    a = BiciMad1.resume()
    print(a)


