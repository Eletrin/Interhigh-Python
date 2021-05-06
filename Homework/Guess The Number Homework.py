import time

print("I am thinking of a number between 1 and 10")
time.sleep(2)
number = int(input("Try and guess my number: "))

while number != 6:
    print("That is not my number")
    time.sleep(1)
    number = int(input("Try and guess my number: "))

if number == 6:
    print("Yay you guessed my number!")
else:
    print("Error Occurred :P")
