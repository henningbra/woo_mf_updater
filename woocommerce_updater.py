import requests
from requests.auth import HTTPBasicAuth
from models.product import Product

URL = "https://www.spraylakk.no/wp-json/wc/v3/"
KEY = "ck_f21327a9209b6e2dd5f52f47178192010227015a"
SECRET = "cs_c98fd392e74f8c46a8c80473e2961844bf515b37"
AUTH = HTTPBasicAuth(KEY, SECRET)

    
if __name__ == "__main__":

    data = {
        'key': '36684',
        'sku': '1234567890123',
        'regular_price': "66.00",
        'sales_price': "50.00",
        'gtin13': 1234567890123,
        'weight': "0.1",
        'length': "0.1",
        'width': "0.2",
        'height': "0.4"
    }

    p = Product(data)
    response = requests.put(URL+p.resource, json=p.data(), auth=AUTH)
    print(response)





