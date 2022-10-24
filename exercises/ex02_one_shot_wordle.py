"""Ex02 --- one shot wordle."""

__author__ = "730481811"

word = "python"

guess_word = input(f"What is your {len(word)}-letter guess? ")

while len(guess_word) != len(word):
    guess_word = input(f"That was not {len(word)} letters! Try again: ")

i = 0
result = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while i < len(word):
    if guess_word[i] == word[i]:
        result = result + GREEN_BOX
    else:
        if guess_word[i] in word:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
    i = i + 1
print(result)

    
if len(guess_word) == len(word):
    if guess_word == word:
        print("Woo! You got it!")
    else: 
        print("Not quite. Play again soon!")