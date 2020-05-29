numbers = [1,2,3,4,5,6,7,8,9,10]
letters = 'ABCDEF'
idx = 0
for number in numbers:
    print(idx, number * 2)
    idx = idx + 1
    if idx > 3:
        break

# for letter in letters:
#     print(letter)

# person = {
#     'name': 'Jack',
#     'surname': 'Mabaso',
#     'age': 54
# }
# keys = person.keys()
# for key in person:
#     print(person[key])

# for key in keys:
#     print(person[key])