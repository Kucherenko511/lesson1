from pprint import pprint

product = {
    'name' : 'iPhone 12',
    'stocks' : 24,
    'price' : 65442.2
}
product['price'] = product['price'] - 60000
pprint(product)