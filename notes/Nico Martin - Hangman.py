import random
guesses = 8

word_list = ["Camera", "Games", "PS4", "XBox", "iPhone", "Android", "Tablet", "Car", "Computer", "Tv"]

hangman_list = random.choice(word_list)

print(hangman_list)

print (len(hangman_list))

import string

print(list(string.ascii_letters))
print(string.digits)
print(string.punctuation)
