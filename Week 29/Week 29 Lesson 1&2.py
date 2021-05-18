# Imports
import time
import random

# Lesson 1
# ---------------------------------------------------------------------------------------------------------------

# Task 1
print("Hello Player, Welcome to the Guess My Number Game :D")
time.sleep(1)
print("I am going to think of a number between 1 to 100")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print("..")
time.sleep(0.5)
print("...")
time.sleep(1)
print("Okay I have thought of one, try and guess it!")

number = random.randint(1, 100)
counter = 0
guess = 0

while guess != number:
    guess = int(input("Answer: "))
    if guess > number:
        print("My number is lower, try again")
    else:
        print("My number is higher, try again")
    counter = counter + 1

if guess == number:
    print("Well done you guessed my number :D")
    print("You took", counter, "attempts")
else:
    print("Error Occurred :P")

# ---------------------------------------------------------------------------------------------------------------

# Lesson 2
# ---------------------------------------------------------------------------------------------------------------

# To Be Continued

# ---------------------------------------------------------------------------------------------------------------
