# -------------------------------------------
# Exercise: Learn about variables in Python
# -------------------------------------------
# This program currently repeats itself and hard-codes data.
# Your task: Use variables to make the code shorter and easier to change!

# Step 1: Run this program as it is first:
name = "Rekha"
age = 25
food = "noodles"
print(f"Hello, {name}!")
print(f"{name} is 25 years old.")
print(f"In 5 years, {name} will be {age + 5}.")
print(f"{name} really likes {food}.")
print(f"{food} is {name}'s favourite food!")

# This will just add an empty line for space
# Please don't touch this
print("")
bobName = "Bob"
bobAge = 30
bobFood = "noodles"
print(f"Hello, {bobName}!")
print(f"{bobName} is {bobAge} years old.")
print(f"In 5 years, Bob will be {bobAge + 5} years old.")
print(f"{bobName} really likes {bobFood}.")
print(f"{bobFood} is Bob's favourite food!")

# Notice there's lots of repetition!
# If we want to change Alice's age or favourite food, we'd have to change it in many places.

# Step 2: Refactor using variables:
# 1. Create variables for name, age, and favourite food.
# 2. Replace the hard-coded text with variables using f-strings.
# Example:
# name = "Alice"
# age = 25
# food = "pizza"
# print(f"Hello, {name}!")
# print(f"{name} is {age} years old.")
# print(f"In 5 years, {name} will be {age + 5} years old.")
# print(f"{name} really likes {food}.")
# print(f"{food.capitalize()} is {name}'s favourite food!")

# Step 3: Do the same for Bob, or make your own second person!
# Use different values for name, age, and food.
sandyName = "Sandy"
sandyAge = 40
sandyFood = "bread"
print(f"Hello, {sandyName}!")
print(f"{sandyName} is {sandyAge} years old.")
print(f"In 5 years, {sandyName} will be {sandyAge + 5} years old.")
print(f"{sandyName} really likes {sandyFood}.")
print(f"{sandyFood} is Sandy's favourite food!")

inputname = input("What is your name? ")
inputage = int(input("How old are you? "))
inputfood = input("What is your favourite food? ")
print(f"Hello, {inputname}! Next year you will be {inputage + 1}.")
print(f"{inputfood.capitalize()} is your favourite food!")

# Step 4: Add a third person with their own data.
# This should now be much quicker since you only need to change variables,
# not rewrite all the print statements.

# -------------------------------------------
# 💡 Extra Challenge (optional):
# - Use input() to ask the user for their name, age, and favourite food.
# - Then print a message using what they typed in!
# Example:
# name = input("What is your name? ")
# age = int(input("How old are you? "))
# food = input("What is your favourite food? ")
# print(f"Hello, {name}! Next year you will be {age + 1}.")
# print(f"{food.capitalize()} is your favourite food!")
# Once you are done, please run the following commands (one by one) in the terminal:
# git add Ex1_variables.py
# git commit -m "Completed variables exericse"
# git push origin main
