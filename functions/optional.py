def calculate(x,y):
    total = 0
    x,y = sorted([x,y])
    for i in range(x,y+1):
        total += i
    
    return total

def say_hello(name = 'Unknown'):
    print('Hello', name)
# say_hello()
# say_hello('Jack')

def get_profile(name = '', age = 25, surname = 'Doe'):
    your_name = name
    if name == '':
        your_name = input('Please enter your name: ')
    full_name = F"{your_name} {surname}"
    print(F"My name is {full_name} and I am {age} years old")

# name = input('Please enter your name: ')
# get_profile(name)
# get_profile('Nkosinathi', '_99', 30)
# get_profile(surname = 'Paul', age = 26)
get_profile('Paul', surname = 'Pokemon')
get_profile(surname = 'Pokemon')