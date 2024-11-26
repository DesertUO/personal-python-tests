import random
import utils
# Minimum and Maximum number
PlayAgain = 1
while PlayAgain != 2:
    # Generate the number (1 < N < 100)
    print("Choose your number range-->")
    vmin = utils.sanitizeInputInt("Enter the minimum number value: ")
    vmax = utils.sanitizeInputInt("Enter the maximum number value: ")
    while vmin >= vmax:
        print("Minimum value must be lower than the maximum one 🤦‍♂️...")
        vmin = utils.sanitizeInputInt("Enter the minimum number value: ")
        vmax = utils.sanitizeInputInt("Enter the maximum number value: ")
    NumberToGuess = random.choice(range(vmin, vmax + 1))
    # Make the player guess
    NumGuessed = None
    while (NumGuessed != NumberToGuess):
        NumGuessed = utils.sanitizeInputInt("Guess a number: ")
        if NumGuessed < NumberToGuess:
            print("Number is too low ⬇️")
        elif NumGuessed > NumberToGuess:
            print("Number is too high ⬆️")

    print("You guessed correctly! 👌")
    PlayAgain = utils.sanitizeInputInt("Do you want to play again 😁?(1 = Yes, 2 = No): ", 1, 2)
print("Thanks for playing! ")
