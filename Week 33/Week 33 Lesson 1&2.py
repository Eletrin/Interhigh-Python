# Lesson 1
# ---------------------------------------------------------------------------------------------------------------

heroes = ["Batman", "Wonder Woman", "Superman", "Spiderman"]

print("Current Pilot:", heroes[0])
print("Current Co-Pilot:", heroes[1])
heroes[2] = "Hit Girl"
heroes.append("Iron Man")
heroes.append("Doctor Strange")
print(heroes)

number = int(input("Which hero do you want to replace? Choose a number from 1-6!"))
number = number-1
heroes[number] = input("What hero do you want to replace them with: ")
print(heroes)

# ---------------------------------------------------------------------------------------------------------------

# Lesson 2
# ---------------------------------------------------------------------------------------------------------------

# Task 1
villains = ["The Joker", "Magneto", "Red Mist", "Doc Ock"]

# Task 2
for counter in range(4):
    print(villains[counter])

# Task 3
wages = [21, 17, 3, 5]

# Task 4
for i in range(4):
    print(villains[i]+": £"+str(wages[i]), "Million")

# Task 5
totalWage = 0

for b in range(4):
    totalWage = totalWage + wages[b]

print("£"+str(totalWage), "Million all together")

# ---------------------------------------------------------------------------------------------------------------
