import random
import string

words = ["Camera", "Games", "PS4", "XBox", "iPhone", "Android", "Tablet", "Car", "Computer", "Tv"]

guesses = 8
letters_guessed = []

answer = random.choice(words)
# print(answer)
output = []

for i in range(len(answer)):
    output.append("*")
print("".join(output))
print(random.choice)
input("Type in a letter: ")
# print(list(string.ascii_letters))
# print(string.punctuation)

