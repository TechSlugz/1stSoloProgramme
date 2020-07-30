import sys, math

# Inputs

name = str(input("What is your name: "))

age = str(input("How old are you: "))

# Conversions

age = int(age)

# Calculations

diff = (100 - age)

year = str((2020 - age)+100)

# Output


print (f"Hay {name} you are currently {age} years old, in {diff} years you will be 100, in the year {year}")
