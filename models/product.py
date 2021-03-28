import json


# adding meta and inherit?
class Meta:
    # GTIN13
    pass


class Model:

    @property
    def resource(self):
        return self.endpoint + self.key

    def data(self):
        return self.__dict__


class Product(Model):

    endpoint = 'products/'

    def __init__(self, kwargs):
        self.key = str(kwargs.pop('key'))
        self.sku = str(kwargs.pop('sku'))
        self.regular_price = str(kwargs.pop('regular_price'))
        self.sales_price = str(kwargs.pop('sales_price'))
        self.dimensions = {
            'length': str(kwargs.pop('length')),
            'width': str(kwargs.pop('width')),
            'height': str(kwargs.pop('height')),
        }
        self.weight = str(kwargs.pop('weight'))
        self.meta_data = []
        self.meta_data.append(
            {
                'key': 'wpseo_global_identifier_values',
                'value': {
                    'gtin13': str(kwargs.pop('gtin13'))
                }
            }
        )


class Product1(Model):

    endpoint = 'products/'

    def __init__(self, kwargs):
        self.key = str(kwargs.pop('key', None))
        self.meta_data = []
        self.meta_data.append(
            {
                'key': '_woosea_gtin',
                'value': str(kwargs.pop('gtin13', None))
            }
        )
        self.meta_data.append(
            {
                'key': '_woosea_ean',
                'value': None
            }
        )
        self.meta_data.append(
            {
                'key': '_woosea_brand',
                'value': str(kwargs.pop('brand', None))
            }
        )


if __name__ == "__main__":

    data = {
        'key': '36684',
        'sku': '1234567890123',
        'regular_price': "66.00",
        'sales_price': "50.00",
        'gtin13': 1234567890444,
        'weight': "0.1",
        'length': "0.1",
        'width': "0.2",
        'height': "0.4"
    }
    
    product = Product(data) 
    print(json.dumps(product.data()))

