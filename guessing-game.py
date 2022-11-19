from random import randint

print("Welcome to Guessing game")
print("We have a number between 1 and 100")
print("Try guessing our number to complete the game")

isGameCompleted = False
numberOfGuesses = 0
guessedNumber = randint(1, 100)

while isGameCompleted == False:
    numberOfGuesses = numberOfGuesses + 1
    numberGuessed = int(input("Guess: " + str(numberOfGuesses) + ". Enter your guess: "))
    if numberGuessed < 1 or numberGuessed > 100:
        print("Number should be between 1 and 100")
    if numberGuessed < guessedNumber:
        print("Your number is less than the number we have")
    elif numberGuessed > guessedNumber:
        print("Your number is greater than the number we have")
    else:
        print("You successfully guessed in " + str(numberOfGuesses) + " guesses.")
        isGameCompleted = True
        print("Game completed!")
