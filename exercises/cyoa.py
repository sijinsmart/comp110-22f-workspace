"""A number guessing game such as the generating a random number and asking the user to guess it and counting the number of attempts it takes them to guess it correctly."""


__author__ = "730481811"


from random import randint

white: str = "\U00002B1C"
green: str = "\U0001F7E9"
yellow: str = "\U0001F7E8"
player: str = ""
points: int = 0


def comparefunc(numberguess: int, numbersecret: int) -> str:
    """Give two integers, to compare their value. If the guessnumber is bigger, return white, if they are the same, return green, if the realnumber is bigger, return yellow."""
    if numberguess == numbersecret:
        print("It is exact the secret number!")
        return green
    if numberguess > numbersecret:
        print("Your number is bigger than the secret number.")
        return white
    else:
        print("Your number is smaller than the secret number.")
        return yellow
    

def input_guess(numberguess: int) -> int:
    """Given an number with "expected range" of (1,100)."""
    while numberguess < 0 or numberguess > 100:
        numberguess = int(input("That wasn't a number between(1,100)! Try again: "))
    return (numberguess)


def greet() -> None:
    """Welcome the player."""
    global player
    if len(player) == 0:
        player = input("What's your name ")
    print(f"Welcome to our game, {player}")


def hardmod(points: int) -> int:
    """Call the hard mode of the game."""
    numbersecret: int = randint(1, 100)
    i: int = 1
    while i < 7: 
        numberguess: int = int(input(f"{player}, enter a integer number between (1,100): "))
        print(f"===Turn {i}/6 ===")
        input_guess(numberguess)
        print(comparefunc(numberguess, numbersecret))
        if numberguess == 0:
            print(f"The secret number is {numbersecret}")
        if numberguess == numbersecret:
            print(f"You won in {i}/6 turns!")
            points = points + 7 - i
            print(f"Thanks for playing. Your points is {points}.")
            i = 7
        i = i + 1
    print("If you want to try a new number: type: 1, \nif you want to quit: type: 2.")
    answer: int = int(input("Type here: "))
    if answer == 1:
        main()
    else:
        return points


def easymod() -> None:
    """Call the easymode of the game."""
    global points
    numbersecret: int = randint(1, 50)
    i: int = 1
    while i < 7: 
        numberguess: int = int(input(f"{player}, enter a integer number between (1,50): "))
        print(f"===Turn {i}/6 ===")
        input_guess(numberguess)
        print(comparefunc(numberguess, numbersecret))
        if numberguess == 0:
            print(f"The secret number is {numbersecret}")
        if numberguess == numbersecret:
            print(f"You won in {i}/6 turns!")
            points = points + 7 - i
            print(f"Thanks for playing. Your points is {points}.")
            i = 7
        i = i + 1
    print("If you want to try a new number: type: 1, \nif you want to quit: type: 2.")
    answer: int = int(input("Type here: "))
    if answer == 1:
        main()
    else:
        print(f"Your total points is {points}.")
        quit()

    
def main() -> None:
    """Connect the functions."""
    greet()
    choice: str = input("Do you want easy/hard or exit? \nWe suggest you to go from easy to hard.")
    if choice == "easy":
        easymod()
    if choice == "hard":
        hardmod(points)
    else:
        print(f"Bye, your total points is {points} ")
        quit()


if __name__ == "__main__":
    main()