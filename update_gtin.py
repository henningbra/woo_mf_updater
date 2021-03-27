import json
import requests
from requests.auth import HTTPBasicAuth
from models.product import Product1

URL = "https://www.spraylakk.no/wp-json/wc/v3/"
KEY = "ck_f21327a9209b6e2dd5f52f47178192010227015a"
SECRET = "cs_c98fd392e74f8c46a8c80473e2961844bf515b37"
AUTH = HTTPBasicAuth(KEY, SECRET)

    
if __name__ == "__main__":

    data = {
        'key': '37384',
        # 'sku': '1234567890123',
        # 'regular_price': "66.00",
        # 'sales_price': "50.00",
        # 'gtin13': 1234567890123,
        # 'weight': "0.1",
        # 'length': "0.1",
        # 'width': "0.2",
        # 'height': "0.4"
    }

    get_response = True
    page = 0
    while get_response is not None:
        page = page + 1
        get_response = requests.get(URL+"products?per_page=10"+"&page="+str(page), auth=AUTH)
        # response = requests.get(URL + "products?per_page=1" + "&page=" + str(page), auth=AUTH)
        parsed = get_response.json()
        for prod in parsed:
            data = dict()
            data['key'] = prod.get('id', None)

            tags = prod.get('tags', [])
            for tag in tags:
                brand = tag['name']
                data['brand'] = brand
                print(brand)

            meta_data = prod.get('meta_data', None)
            for item in meta_data:
                ean = 'missing'
                if item['key'] == 'wpseo_global_identifier_values':
                    ean = item['value']['gtin13']
                    data['gtin13'] = ean
                    print(ean)

            update_product = Product1(data)
            put_response = requests.put(URL + update_product.resource, json=update_product.data(), auth=AUTH)
            print(put_response)

        #print(len(parsed))
    # parsed = response.json()
    # print(json.dumps(parsed, indent=4, sort_keys=True))
    # 
    # "meta_data": [

        # {
        #     "id": 253963,
        #     "key": "wpseo_global_identifier_values",
        #     "value": {
        #         "gtin12": "",
        #         "gtin13": "7610567930066",
        #         "gtin14": "",
        #         "gtin8": "",
        #         "isbn": "",
        #         "mpn": ""
        #     }
        # }

