from bicimad.UrlEMT import UrlEMT
from bicimad.BiciMad import BiciMad

if __name__ == "__main__":
    cosa = UrlEMT()
    var1 = cosa.get_url(1, 23)
    print(var1)
    var2 = cosa.get_csv(1, 23)
    print(var2)
