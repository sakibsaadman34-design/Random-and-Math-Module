import random

playing = True

number = str(random.randint(1, 9))

print("I picked a random number from 1 to 9.")
print("Now you will have to guess the number")
print()

while playing:
    guess = input("Enter Your Guess: ")
    if guess == number:
        print("Congrats!")
        print("You Have Guessed The Number")
        print()
        break
    else:
        print("You did not guess it right")
        print("Try Again.")
        print()
        continue