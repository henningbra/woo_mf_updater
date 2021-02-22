import json

# adding meta and inherit?
class Meta:
    # GTIN13
    pass
            
class Product:
    def __init__(self, data):
        self.key = data.pop('key')
        self.sku = data.pop('sku')
        self.regular_price = data.pop('regular_price')
        self.sales_price = data.pop('sales_price')
        self.weight = data.pop('weight')
        self.dimensions = {
            'length': data.pop('length'),
            'width': data.pop('width'),
            'height': data.pop('height'),
        }
        self.meta_data = []
        self.meta_data.append(
            {
                'key': 'wpseo_global_identifier_values',
                'value': {
                    'gtin13': data.pop('gtin13')
                }
            }
        )    

    def data(self):
        return self.__dict__


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
    
    product = Product(data) 
    print(json.dumps(product.data()))

