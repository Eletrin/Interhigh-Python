# Imports
import random

# Lesson 1
# ---------------------------------------------------------------------------------------------------------------

# Task 1
guess = int(input("Enter: "))
number = 4

while guess != number:
    print("Wrong, try again!")
    guess = int(input("Enter: "))

# ---------------------------------------------------------------------------------------------------------------

# Lesson 2
# ---------------------------------------------------------------------------------------------------------------

# Task 1
number = random.randint(1, 10)
counter = 1

name = input("Hello and welcome to my game! May I get your name? ")

for x in range(1, 6):
    guess = int(input('Please enter a guess between 1 and 10: '))
    if guess == number:
        print('Well done', name + ", It took you", counter, "tries.")
        break
    else:
        print('Hard luck')
        counter = counter + 1

# Task 2
name = input("May I please get your name? ")

for x in range(1, 7):
    print(name)

# Task 3
no1 = float(input("1st number: "))
no2 = float(input("2nd number: "))
no3 = float(input("3rd number: "))
no4 = float(input("4th number: "))
no5 = float(input("5th number: "))

fullnumber = no1 + no2 + no3 + no4 + no5
finalnumber = fullnumber / 5

print("The average of all of those numbers you gave me are", finalnumber)

# ---------------------------------------------------------------------------------------------------------------
