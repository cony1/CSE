import random
r = random.randint(1, 10)
print("Guess a random number. You 5 guess's to find out")
guess = 5
playing = True


while guess > 0 and playing:
   guess = int(input("Guess="))

   if guess > r:
     print("Lower")
     guess = guess - 1


else :guess < r
print("Greater")
    guess = guess - 1

else
     print("Correct")
     playing = false

    if guess == 0:
        print("Try Again")

guess = 5
playing = True
while guess > 0 and playing:\
    guess = input

