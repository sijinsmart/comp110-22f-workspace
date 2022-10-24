"""Ex01 - Chardle - A cute step toward."""

__author__ = "730481811"

word = input("Enter a 5-character word: ")
if len(word) < 5 or len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()

single_cha = input("Enter a single character: ")
if len(single_cha) < 1 or len(single_cha) > 1:
    print("Error: Character must be a single character.")
    exit()
    
print("Searching for " + str(single_cha) + " in " + str(word))

count: int = 0

if str(single_cha) == word[0]:
    count = count + 1
    print(str(single_cha) + " found at index 0")

if str(single_cha) == word[1]:
    count = count + 1
    print(str(single_cha) + " found at index 1")

if str(single_cha) == word[2]:
    count = count + 1
    print(str(single_cha) + " found at index 2")

if str(single_cha) == word[3]:
    count = count + 1
    print(str(single_cha) + " found at index 3")

if str(single_cha) == word[4]:
    count = count + 1
    print(str(single_cha) + " found at index 4")


if count == 1:
    print(str(count) + " instance of " + str(single_cha) + " found in " + str(word))
elif count > 1:
    print(str(count) + " instances of " + str(single_cha) + " found in " + str(word))
else:
    print("No instances of " + str(single_cha) + " found in " + str(word))