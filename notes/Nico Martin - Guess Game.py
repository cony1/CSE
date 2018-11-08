import random
r = random.randinnt(1,100)
print ("Guess a random number. You 5 guess's to find out")

if guess > random.randint(1,100):
    print ("Lower")

elif guess < random.radint(1,10):
    print ("Greater")

else:
    print ("Correct")
guesses_left = 5
playing = True
while guesses_left > 0 and playing:
    guess = input   