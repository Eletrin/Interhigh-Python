# Lesson 1
# ---------------------------------------------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------------------

# Lesson 2
# ---------------------------------------------------------------------------------------------------------------

# Worksheet one completed in first lesson

# Main Lesson:

correctPassword = "pa55word"
guesses = 0
guess = ""

while guess != correctPassword:
	guess = input("Password: ")
	guesses = guesses + 1

print("Access Granted")

if guesses == 1:
	print("That took 1 guess.")
else:
	print("That took you", str(guesses), "goes.")

# ---------------------------------------------------------------------------------------------------------------
