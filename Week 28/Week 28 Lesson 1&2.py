# Imports
import time
import random

# Lesson 1
# ---------------------------------------------------------------------------------------------------------------

# Task 1
answer = input("What is the capital of France? ")
answer = answer.title()
counter = 0

while answer != "Paris":
    answer = input("Incorrect, try again: ")
    answer = answer.title()
    counter = counter + 1

print("Correct! Well done.")

answer = input("What comes after A in the alphabet? ")
answer = answer.title()

while answer != "B":
    answer = input("Incorrect, try again: ")
    answer = answer.title()
    counter = counter + 1

print("Correct! Well done.")

answer = input("What's 9+10? ")
answer = answer.title()

while answer != "21":
    answer = input("Incorrect, try again: ")
    answer = answer.title()
    counter = counter + 1

print("Ya Stoopid. :P")

answer = input("What is 4x9? ")
answer = answer.title()

while answer != "36":
    answer = input("Incorrect, try again: ")
    answer = answer.title()
    counter = counter + 1

print("Correct! Well done.")

answer = input("When did WWII end? ")
answer = answer.title()

while answer != "1945":
    answer = input("Incorrect, try again: ")
    answer = answer.title()
    counter = counter + 1

print("Correct! Well done.")
print("You finished the quiz with", counter, "mistakes!")

# ---------------------------------------------------------------------------------------------------------------

# Lesson 2
# ---------------------------------------------------------------------------------------------------------------

# Task 1
attempts = 0

while password != "Billy" or attempts != 3:
    password = input("Password: ")
    if password == "Billy":
        print("Access Granted")
    else:
        print("Access Denied")
    attempts = attempts + 1

if attempts == 3:
    print("MACHINE LOCKED")
else:
    print("Error Occurred :P")

# Task 2
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
guess = "UNDEFINED"

while guess != number:
    guess = int(input("Answer: "))
    if guess > number:
        print("My number is higher, try again")
    else:
        print("My number is lower, try again")
    counter = counter + 1

if guess == number:
    print("Well done you guessed my number :D")
    print("You took", counter, "attempts")
else:
    print("Error Occurred :P")

# ---------------------------------------------------------------------------------------------------------------
