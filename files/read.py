data = open('data.txt', 'r')
print(data.readline())
print(data.readline())
data.seek(0)
print(data.readlines())



# print(data.read())
# data.seek(0)
# print(data.read())
# print(data.read())