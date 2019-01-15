"""
print("Hello World")

# Hello World

cars = 5
driving = True

print("I have %d cars" % cars)
print("I have" + str(cars) + "cars")

age = input("How old are you?")
print(age + "??? You really shouldn't lie about your age.")

colors = ["blue", "red", "white", "black"]
colors.append("green")
print(colors)
colors.pop(0)
print(colors)
print(colors[2])

print(len(colors))
"""

import string

print(list(string.ascii_letters))
print(string.digits)
print(string.punctuation)
