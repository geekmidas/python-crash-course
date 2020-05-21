barcodes = {
    '100': 'apple',
    '101': 'kiwi',
    '102': 'pear',
}
# Converts dict_keys to a list AKA: Type casting
keys = list(barcodes.keys())
number = '50.99999999'
# converts string to a float
a = float(number)
another_number = 56
total = int(a) + another_number
print(total, int(a))
print(keys, keys[0])
items = list(barcodes.items())
print(type(a))
