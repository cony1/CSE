import random
r = random.randint(1, 10)
print("Guess a random number. You 5 guess's to find out")
guess = 5
playing = True


while guess_left > 0 and playing:
   guess = int(input("Guess="))

   if guess > r:
   print("Lower")
    guesses_left = guesses_left -10
   |7

elif guess > r:
   print("Greater")
    guesses_left = guesses_left -1
else:
    print("Correct")

guesses_left = 5
playing = True
while guesses_left > 0 and playing:\
    guess = input
