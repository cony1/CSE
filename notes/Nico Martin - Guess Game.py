import random
r = random.randint(1, 10)
print("Guess a random number. You 5 guess's to find out")
guess = 5

if guess > random.randint(1, 10):
    print("Lower")

elif guess < random.randint(1, 10):
    print("Greater")

else:
    print("Correct")

guesses_left = 5
playing = True
while guesses_left > 0 and playing:\
    guess = input
