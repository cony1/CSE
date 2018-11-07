import random
r = random.randint(1,100)
print ("Guess a random number. You 5 guess's to find out")

if guess > random.randint(1,100):

guesses_left = 5
playing = True
while guesses_left > 0 and playing:
    guess = input