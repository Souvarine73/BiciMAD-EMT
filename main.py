from bicimad.UrlEMT import UrlEMT

if __name__ == "__main__":
    cosa = UrlEMT()
    cosa.select_valid_urls()
    var = cosa.set_valid_urls
    print(var)
    url = cosa.get_url(1, 23)
    print(url)
    csv = cosa.get_csv(12, 23)
    print(csv)
