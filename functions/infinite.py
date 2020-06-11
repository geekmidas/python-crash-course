def _calculate(x = 0,y = 0,z = 0):
    return x + y + z

def calculate(*numbers):
    total = 0
    for number in numbers:
        total += number

    return total
# some_itr = 'ABC' and key = 'B', return 1
# some_itr = [1,2,3,4,5] and key = 6, return -1
def search(some_itr, key):
    # Return the position of the key in
    # some_itr or -1 when key is not found
    pass

print(calculate(1,2,3))