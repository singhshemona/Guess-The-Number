#use a while statement
import random as rd

guessesTaken = 1
randomNumber = rd.randint(1, 20)

print("Hello! What is your name?")
myName = input()

print("Well " + myName + ", I am thinking of a number between 1 and 20.")

while guessesTaken < 5:
    print("Take a guess: ")
    guess = int(input())
    if guess < randomNumber:
        print("Your guess is too low.")
    elif guess > randomNumber:
        print("Your guess is too high.")
    else:
        print("Good job! You guessed my number in " + str(guessesTaken) + " guesses!")
        break
    guessesTaken = guessesTaken + 1

if guess == randomNumber:
    print("Good job, " + myName + "! You guessed my number in " + str(guess))
else:
    print("Nope. The number I was thinking of was " + str(randomNumber))
