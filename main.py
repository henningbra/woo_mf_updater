import pandas as pd


df = pd.read_excel('book.xlsx', index_col=None)
print(df)
dct = df.to_dict('records')
print(dct)

if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    from models.product import Product

    URL = "https://www.spraylakk.no/wp-json/wc/v3/"
    KEY = "ck_f21327a9209b6e2dd5f52f47178192010227015a"
    SECRET = "cs_c98fd392e74f8c46a8c80473e2961844bf515b37"
    AUTH = HTTPBasicAuth(KEY, SECRET)

    p = Product(dct[0])
    response = requests.put(URL+p.resource, json=p.data(), auth=AUTH)
    print(response.text)
