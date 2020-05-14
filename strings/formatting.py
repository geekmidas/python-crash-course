my_salary = 100
tax_rate = 0.18

net_salary = my_salary * (1 - tax_rate)

name = "Jack"
words = " your salary is "
full_word = name + words + str(my_salary)

print(full_word)
print("{} your salary is {}".format(name, my_salary))
print("{0} your salary is {1}".format(name, my_salary))
print("{name} your salary is {salary}".format(name = name, salary = my_salary))
print(F"{name} your salary is {my_salary}")
