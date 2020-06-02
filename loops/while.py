number =  16
while number > 2:
    x = number
    number = number - 1
    if x % 3 == 0:
        continue # skip
    print(x, 'Something')
