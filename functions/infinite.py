def _calculate(x = 0,y = 0,z = 0):
    return x + y + z

def calculate(*numbers):
    total = 0
    for number in numbers:
        total += number

    return total
# some_itr = 'ABC' and key = 'B', return 1
# some_itr = [1,2,3,4,5] and key = 6, return -1
def search_one(some_itr, key):
    # Return the position of the key in
    # some_itr or -1 when key is not found
    size = len(some_itr)
    for i in range(size):
        value = some_itr[i]
        if value == key:
            return i
    return -1

def search_two(some_itr, key):
    # Return the position of the key in
    # some_itr or -1 when key is not found
    i = 0
    for value in some_itr:
        if value == key:
            return i
        i += 1
    return -1

def search_three(some_itr, key):
    # Return the position of the key in
    # some_itr or -1 when key is not found
    i = 0
    result = -1
    for value in some_itr:
        if value == key:
            result = i
            break
        i += 1
    return result

def search_four(some_itr, key):
    # Return the position of the key in
    # some_itr or -1 when key is not found
    items = enumerate(some_itr)
    for i,value in items:
        if value == key:
            return i
    return -1

numbers = [1,2,3,4,5]
key = 2
# print(search_one(numbers, key))
# print(search_two(numbers, key))
# print(search_three(numbers, key))
# print(search_four(numbers, key))
items = zip('ABC', [1,2,2,50], (1,2,3,4,5))
print(list(items))
