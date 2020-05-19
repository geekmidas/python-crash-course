name = 'Sara'
score = 10

print("{} scored {} points".format(name,score))
print("{0} scored {1} points".format(name,score))
print("{1} scored {0} points".format(score,name))
print("{name} scored {score} points".format(name = name,score = score))
print(F"{name} scored {score} points")

age = 27
name = 'hlabirwa'
print(name.split('a'))
print("{name} is {age} years of age".format(name = name,age = age))

correct_name = name[0].upper() + name[1:]
broken_name = 'hlaBirwA'
fixed_name = broken_name[0].upper() + broken_name[1:].lower()
print(broken_name, correct_name, name.capitalize(), broken_name.capitalize(), fixed_name)