import json


# adding meta and inherit?
class Meta:
    # GTIN13
    pass


class Model:

    @property
    def resource(self):
        return self.endpoint + str(self.key)

    def data(self):
        return self.__dict__


class Product(Model):

    endpoint = 'products/'

    def __init__(self, kwargs):
        self.key = kwargs.pop('key')
        self.sku = kwargs.pop('sku')
        self.regular_price = kwargs.pop('regular_price')
        self.sales_price = kwargs.pop('sales_price')
        self.dimensions = {
            'length': kwargs.pop('length'),
            'width': kwargs.pop('width'),
            'height': kwargs.pop('height'),
        }
        self.weight = kwargs.pop('weight')
        self.meta_data = []
        self.meta_data.append(
            {
                'key': 'wpseo_global_identifier_values',
                'value': {
                    'gtin13': kwargs.pop('gtin13')
                }
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

