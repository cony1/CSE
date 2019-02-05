import random
import string

words = ["Camera", "Games", "PS4", "XBox", "iPhone", "Android", "Tablet", "Car", "Computer", "Tv"]

guesses = 8
letters_guessed = []

answer = random.choice(words)
letters_in_answer = list(answer)
# print(answer)
output = []

for i in range(len(answer)):
    output.append("*")

print(answer)
while guesses > 0:
    print(letters_in_answer)
    print("".join(output))

    current_guess = input("Type in a letter:")
    letters_guessed.append(current_guess)
    if current_guess in answer:
        print("Correct!")
    else:
        print("Nope.")
        guesses -= 1

    if answer is letters_in_answer:
        print(letters_in_answer)

    else:
        print("")

# print(list(string.ascii_letters))
# print(string.punctuation)
