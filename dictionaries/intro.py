prices = {
    'apple': 1.99,
    'kiwi': 0.50,
    'pear': 2.0
}
barcodes = {
    '100': 'apple',
    '101': 'kiwi',
    '102': 'pear',
}

print(prices)
print(prices['apple'])

barcode = '100'
product = barcodes[barcode]
price = prices[product]
print(prices[barcodes[barcode]])
print(price)
prices['banana'] = 5.0
prices['apple'] = 5.0
print(prices.get('banana'))
print(prices)
