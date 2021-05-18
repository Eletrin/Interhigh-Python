# Imports
import time
import random

# Lesson 1
# ---------------------------------------------------------------------------------------------------------------

# Task 1
print("      *****************************")
print("          Guess My Number Game")
print("      *****************************")
print("I Have Thought Of A Number Between 1 And 100")
print("")

number = random.randint(1, 100)
counter = 1
guess = int(input("Answer: "))

while guess != number:
    if guess > number:
        print("My number is lower, try again!")
    else:
        print("My number is higher, try again!")
    guess = int(input("Answer: "))
    counter = counter + 1

if guess == number:
    print(" ")
    print("Well done you guessed my number :D")
    print("You took", counter, "attempts")
else:
    print("Error Occurred :P")

# ---------------------------------------------------------------------------------------------------------------

# Lesson 2
# ---------------------------------------------------------------------------------------------------------------

# To Be Continued

# ---------------------------------------------------------------------------------------------------------------
