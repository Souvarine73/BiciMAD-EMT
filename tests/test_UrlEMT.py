import io

from bicimad import UrlEMT
import pytest
import requests


def test_init():
    urlemt_check = UrlEMT()
    set_urls = urlemt_check.urls
    set_check = {'/getattachment/ab3776ab-ba7f-4da3-bea6-e70c21c7d8be/trips_21_06_June-csv.aspx',
                 '/getattachment/845c3697-cb16-45b5-84f6-69e45c7aa525/trips_21_11_November-csv.aspx',
                 '/getattachment/34b933e4-4756-4fed-8d5b-2d44f7503ccc/trips_22_12_December-csv.aspx',
                 '/getattachment/e1ea5e02-4ba9-471a-bb95-8cb327220b05/trips_22_03_March-csv.aspx',
                 '/getattachment/7c0b2ce4-520d-4dc1-b29b-c5fa8e798e81/trips_22_10_October-csv.aspx',
                 '/getattachment/a829afec-cac8-427f-80ab-b5cb441514e9/trips_22_02_February-csv.aspx',
                 '/getattachment/cfad5ecf-b5ca-44da-8be3-1983e46646e9/trips_22_07_July-csv.aspx',
                 '/getattachment/20b8509b-97a8-4831-b9d2-4900322e1714/trips_23_01_January-csv.aspx',
                 '/getattachment/a1ff7edc-016f-4510-b986-66b957d6f3ec/trips_21_07_July-csv.aspx',
                 '/getattachment/359c458b-1425-4fe9-b2fb-1e2f6d9cd40e/trips_22_08_August-csv.aspx',
                 '/getattachment/7a88cb04-9007-4520-88c5-a94c71a0b925/trips_23_02_February-csv.aspx',
                 '/getattachment/45f51cef-9296-4afe-b42e-d8d5bca3c548/trips_22_11_November-csv.aspx',
                 '/getattachment/51ba4be6-596f-41d3-8bab-634c4be569c5/trips_21_10_October-csv.aspx',
                 '/getattachment/0417f179-9741-44ba-8f8c-0bc9fc2b06fe/trips_21_12_December-csv.aspx',
                 '/getattachment/6cf382ce-44a8-4263-96b4-6beff2610ce7/trips_22_05_May-csv.aspx',
                 '/getattachment/92eeacdb-0723-4832-a8e9-dc3c7ee7a5d3/trips_22_04_April-csv.aspx',
                 '/getattachment/00ac3096-cdb7-4e1b-930a-630cf6e5f8ce/trips_21_09_September-csv.aspx',
                 '/getattachment/31a9c669-b9ba-45f3-bc83-24ac1c357bc6/trips_22_06_June-csv.aspx',
                 '/getattachment/ffa0a05e-f2aa-4a02-a1f7-65525524552e/trips_22_01_January-csv.aspx',
                 '/getattachment/9b1d14ef-90bc-4365-8f8b-612cd2f15863/trips_21_08_August-csv.aspx',
                 '/getattachment/8d9ed4a4-6770-4307-92f8-6e34b6006eea/trips_22_09_September-csv.aspx'}

    for link in set_check:
        assert link in set_urls

def test_get_links():
    url = "https://opendata.emtmadrid.es/Datos-estaticos/Datos-generales-(1)"
    try:
        response = requests.get(url)
        links = UrlEMT.get_links(response.text)
        assert len(links) == 21
    except requests.exceptions.RequestException as e:
        assert False, f"Error en la solicitud HTTP: {e}"


def test_select_valid_urls():
    set_urls = UrlEMT.select_valid_urls()
    set_check = {'/getattachment/ab3776ab-ba7f-4da3-bea6-e70c21c7d8be/trips_21_06_June-csv.aspx',
                 '/getattachment/845c3697-cb16-45b5-84f6-69e45c7aa525/trips_21_11_November-csv.aspx',
                 '/getattachment/34b933e4-4756-4fed-8d5b-2d44f7503ccc/trips_22_12_December-csv.aspx',
                 '/getattachment/e1ea5e02-4ba9-471a-bb95-8cb327220b05/trips_22_03_March-csv.aspx',
                 '/getattachment/7c0b2ce4-520d-4dc1-b29b-c5fa8e798e81/trips_22_10_October-csv.aspx',
                 '/getattachment/a829afec-cac8-427f-80ab-b5cb441514e9/trips_22_02_February-csv.aspx',
                 '/getattachment/cfad5ecf-b5ca-44da-8be3-1983e46646e9/trips_22_07_July-csv.aspx',
                 '/getattachment/20b8509b-97a8-4831-b9d2-4900322e1714/trips_23_01_January-csv.aspx',
                 '/getattachment/a1ff7edc-016f-4510-b986-66b957d6f3ec/trips_21_07_July-csv.aspx',
                 '/getattachment/359c458b-1425-4fe9-b2fb-1e2f6d9cd40e/trips_22_08_August-csv.aspx',
                 '/getattachment/7a88cb04-9007-4520-88c5-a94c71a0b925/trips_23_02_February-csv.aspx',
                 '/getattachment/45f51cef-9296-4afe-b42e-d8d5bca3c548/trips_22_11_November-csv.aspx',
                 '/getattachment/51ba4be6-596f-41d3-8bab-634c4be569c5/trips_21_10_October-csv.aspx',
                 '/getattachment/0417f179-9741-44ba-8f8c-0bc9fc2b06fe/trips_21_12_December-csv.aspx',
                 '/getattachment/6cf382ce-44a8-4263-96b4-6beff2610ce7/trips_22_05_May-csv.aspx',
                 '/getattachment/92eeacdb-0723-4832-a8e9-dc3c7ee7a5d3/trips_22_04_April-csv.aspx',
                 '/getattachment/00ac3096-cdb7-4e1b-930a-630cf6e5f8ce/trips_21_09_September-csv.aspx',
                 '/getattachment/31a9c669-b9ba-45f3-bc83-24ac1c357bc6/trips_22_06_June-csv.aspx',
                 '/getattachment/ffa0a05e-f2aa-4a02-a1f7-65525524552e/trips_22_01_January-csv.aspx',
                 '/getattachment/9b1d14ef-90bc-4365-8f8b-612cd2f15863/trips_21_08_August-csv.aspx',
                 '/getattachment/8d9ed4a4-6770-4307-92f8-6e34b6006eea/trips_22_09_September-csv.aspx'}

    for link in set_check:
        assert link in set_urls


def test_get_url():
    urlemt_test = UrlEMT()
    link = urlemt_test.get_url(2, 23)
    expected = ('https://opendata.emtmadrid.es/getattachment/7a88cb04-9007-4520-88c5-a94c71a0b925/trips_23_02_February'
                '-csv.aspx')
    assert link == expected


def test_get_url_errors():
    with pytest.raises(ValueError):
        urlemt_test = UrlEMT()
        urlemt_test.get_url(13, 22)
        urlemt_test.get_url(2, 25)
        urlemt_test.get_url(12, 23)


def test_get_csv():
    urlemt_test = UrlEMT()
    result = urlemt_test.get_csv(1,23)
    assert isinstance(result, io.StringIO)
