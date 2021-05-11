# Imports
import time
import random

# Lesson 1
# ---------------------------------------------------------------------------------------------------------------

# Task 1
speed = int(input("What speed are you going at? "))

if speed >= 70:
    print("You owe the caught money for speeding! >:(")
else:
    print("Good job, make sure to stay within the speed limit! :)")

# Task 2
grade = int(input("Enter your grade: "))

if grade >= 80:
    print("Distinction")
elif grade >= 70:
    print("Merit")
elif grade >= 60:
    print("Pass")
else:
    print("Fail")

# ---------------------------------------------------------------------------------------------------------------

# Lesson 2
# ---------------------------------------------------------------------------------------------------------------

# Task 1
answer = int(input("What is 2 + 2? "))

if answer == 4:
    print("Well Done")
else:
    print("Sorry the answer was 4")

# Task 2
print("I am thinking of a number between 1 and 10")
time.sleep(2)
guess = int(input("Try and guess my number: "))
number = random.randint(1, 10)

while guess != number:
    print("That is not my number")
    time.sleep(1)
    guess = int(input("Try and guess my number: "))

if guess == number:
    print("Yay you guessed my number!")
else:
    print("Error Occurred :P")


# ---------------------------------------------------------------------------------------------------------------
