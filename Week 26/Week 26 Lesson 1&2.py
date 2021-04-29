# Lesson 1
# ---------------------------------------------------------------------------------------------------------------

money = 15
print("You have £" + str(money))

# ---------------------------------------------------------------------------------------------------------------

# Lesson 2
# ---------------------------------------------------------------------------------------------------------------

username = float(input("What is your username? "))
network = float(input("What network are you using? "))
numberofmins = int(input("How many minutes have you used this month? "))
numberoftexts = int(input("How many texts have you sent in the past month? "))
numberofmins = numberofmins * 0.10
numberoftexts = numberoftexts * 0.05
cost = numberofmins + numberoftexts
vat = cost/5
costwithvat = cost + vat
print(costwithvat)

# ---------------------------------------------------------------------------------------------------------------
