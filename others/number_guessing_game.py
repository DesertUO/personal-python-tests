import random

def InputCheckInt(msg, vmin = -9999999999999, vmax = 9999999999999):
    while True:
        try:
            Num = int(input(msg))
            if Num < vmin or Num > vmax:
                print(f"Please enter a number between {vmin} and {vmax}.")
            else:
                return Num
        except ValueError:
            print("ERROR. Input must be an integer.")

# Minimum and Maximum number
PlayAgain = 1
while PlayAgain != 2:
    # Generate the number (1 < N < 100)
    print("Choose your number range-->")
    vmin = InputCheckInt("Enter the minimum number value: ")
    vmax = InputCheckInt("Enter the maximum number value: ")
    while vmin >= vmax:
        print("Minimum value must be lower than the maximum one 🤦‍♂️...")
        vmin = InputCheckInt("Enter the minimum number value: ")
        vmax = InputCheckInt("Enter the maximum number value: ")
    NumberToGuess = random.choice(range(vmin, vmax + 1))
    # Make the player guess
    NumGuessed = None
    while (NumGuessed != NumberToGuess):
        NumGuessed = InputCheckInt("Guess a number: ")
        if NumGuessed < NumberToGuess:
            print("Number is too low ⬇️")
        elif NumGuessed > NumberToGuess:
            print("Number is too high ⬆️")

    print("You guessed correctly! 👌")
    PlayAgain = InputCheckInt("Do you want to play again 😁?(1 = Yes, 2 = No): ", 1, 2)

print("Thanks for playing! ")