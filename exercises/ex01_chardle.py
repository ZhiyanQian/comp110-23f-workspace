"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730631142"

word = input("Enter a five-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter = input("Enter a single letter: ")
if  len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
    
sum = 0

if word[0] == letter:
    print(letter + " found at index 0")
    sum = sum + 1
if word[1] == letter:
    print(letter + " found at index 1")
    sum = sum + 1
if word[2] == letter:
    print(letter + " found at index 2")
    sum = sum + 1
if word[3] == letter:
    print(letter + " found at index 3")
    sum = sum + 1
if word[4] == letter:
    print(letter + " found at index 4")
    sum = sum + 1

if sum > 0:
    print(str(sum) + " instances of " + letter + " found in " + word)
else:
    print("No instances of " + letter + " found in " + word)