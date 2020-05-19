numbers = [1,2,3,4,5,6,7,8]
fruits = ['Apple', 'Kiwi', 'Pear', 'Banana']
mixed = ['a', '50', 'b', '1','11','4']
name = 'Mike'
print(numbers)
numbers[0] = 50
print(numbers)
numbers.append(9)
numbers.append(9)
print(numbers)
numbers.pop(1)
numbers.pop(1)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
mixed.sort()
print(mixed)

nested = [1,2,3,4, [5,6,7,8]]
a = [1,2,3,4]
b = [5,6,7,8]
c = a + b
print(c)
print(nested[4][1])