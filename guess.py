
import random


print("========================")
print("    Guess the Number    ")
print("   By Darrick Russell   ")
print("========================")
print("")

name = input("What is your name?")
print("")
print("I'm thinking of a number between 0 and 100. Can you guess it?")
the_number = random.randint(1,99)

guess = -1

while guess != the_number:
    guess_text = input("What is your guess?")
    guess = int(guess_text)

    elif guess > 100 or guess < 0:
        print("Please choose a number that is between 0 and 100")
    elif guess < the_number:
        print(f"Sorry {name}, but your guess is too LOW. Try again.")
    elif guess > the_number:
        print(f"Sorry {name}, but your guess is too HIGH. Try again.")
    elif guess > 100 or guess < 0:
        print("Please choose a number that is between 0 and 100")
    else:
        print(f"You guessed it! Congratulations, {name}!")
print("Thanks for playing!")