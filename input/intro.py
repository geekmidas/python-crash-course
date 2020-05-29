
name = 'Jack'
tax_rate = 0.18

my_salary = input("What is your monthly salary: ")
net_salary = float(my_salary) * (1 - tax_rate)
print(F"{name} earns R{my_salary} every month, but takes home R{net_salary}")

