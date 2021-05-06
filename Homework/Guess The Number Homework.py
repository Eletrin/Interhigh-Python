import time
import random

print("I am thinking of a number between 1 and 10")
time.sleep(2)
guess = int(input("Try and guess my number: "))
number = random.randint(1, 10)

while guess != number:
    print("That is not my number")
    time.sleep(1)
    number = int(input("Try and guess my number: "))

if guess == number:
    print("Yay you guessed my number!")
else:
    print("Error Occurred :P")
