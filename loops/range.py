numbers = [1,2,3,4,5,6,7,8,9,0]
fruits = ['Banana', 'Kiwi', 'Orange', 'Pear']

size = len(fruits)

for i in range(1,size):
    print(i, fruits[i])

for i in range(1,10,2):
    print(i)

# Sum all numbers between 1 and 100
total = 1
for i in range(1,101):
    total += i # total = total + i

print(total)