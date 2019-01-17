import random
import string

word_list = ["Camera", "Games", "PS4", "XBox", "iPhone", "Android", "Tablet", "Car", "Computer", "Tv"]

guesses = 8
LettersCorrect = []
LettersIncorrect = []


hangman_list = random.choice(word_list)

print(hangman_list)

print(len(hangman_list))

print(list(string.ascii_letters))
print(string.punctuation)

for i in range(len(hangman_list)):
    if hangman_list[i] == string.ascii_letters:
        hangman_list.pop(i)
        hangman_list.insert(i, "*")

print(hangman_list)
