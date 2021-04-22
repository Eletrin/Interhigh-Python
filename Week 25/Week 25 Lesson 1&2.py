import random
import time

# Prints a welcome message
print("Hello I am Bot! :3")
# Waits 1 second by importing time
time.sleep(1)
# Asks for your firstname and surname and combines them to get your full name
firstname = input("What is your first name? ")
lastname = input("And your surname? ")
fullname = firstname + " " + lastname
# Prints a final statement using the full name
print("Hello", fullname + ",", "It is very nice to meet you!")
