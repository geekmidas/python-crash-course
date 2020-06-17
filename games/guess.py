import random
# random.randint(1,5)

def guess_the_number(start, stop):
    random_number = random.randint(start,stop)
    for number in range(3):
        guess = int(input(F'Please enter a number between {start} and {stop}: '))
        if random_number == guess:
            print(F'You guessed it in attempt number {number + 1}')
            return
    print(F'You failed to guess. The number is {random_number}')

guess_the_number(1,10)