"""Exercise03 _ wordle."""

__author__ = "730481811"


def contains_char(wordsecret: str, single_char: str) -> bool:
    """A string that is being searched through for the second parameter. A string that is expected to be a single character in length and is the character being searched for."""
    assert len(single_char) == 1
    if single_char in wordsecret:
        return True
    else:
        return False


white: str = "\U00002B1C"
green: str = "\U0001F7E9"
yellow: str = "\U0001F7E8"


def emojified(wordguess: str, wordsecret: str) -> str:
    """Give two strings of equal length, first a guess and second a secret, will return a str of emoji."""
    assert len(wordguess) == len(wordsecret)
    i = 0
    color = ""
    while i < len(wordsecret):
        if wordguess[i] == wordsecret[i]:
            color = color + green
        else:
            a = contains_char(wordsecret, wordguess[i])
            if a:
                color = color + yellow
            else:
                color = color + white
        i = i + 1 
    return color


def input_guess(guess: int) -> str:
    """Given an integer "exoected length" of a guess as a parameter."""
    wordguess = input(f"Enter a {guess} character word: ")
    while len(wordguess) != int(guess):
        wordguess = input(f"That wasn't {guess} chars! Try again: ")
    return (wordguess)


def main() -> None:
    """Connect the functions."""
    wordsecret = "codes"
    i = 1
    while i < 7:
        print(f"===Turn {i}/6 ===")
        wordguess = input_guess(5)
        print(emojified(wordguess, wordsecret))
        if wordguess == wordsecret:
            print(f"You won in {i}/6 turns!")
            return
        i = i + 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()