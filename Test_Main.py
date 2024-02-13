import random
import pyautogui

# making a list of all possible words with different difficulties
easyWords = ["log", "word", "phone", "board", "mouse"]
midWords = ["block", "poster", "lumber", "marker", "blanket"]
hardWords = ["keyboard", "parliament", "ministry", "infrastructure", "internal"]
words = [easyWords, midWords, hardWords]

# declaring variables to use later
easy = 0
mid = 1
hard = 2

count = 0
count1 = 0
mistakes = 0
mistakes1 = 0

word = ""
letters = []
rnd = 0
i = ""
j = 0
k = 0

# a function to generate a random word no matter the difficulty
def wordGen(y):
    global word
    global letters
    global rnd

    rnd = random.randint(0, 4)
    word = words[y][rnd]
    letters = list(word)

# function that prints the word using only a "-" symbol
def printWord():
    global i
    global word

    for i in word:
        print("-", end="")
    print()

# function that fills up a list with "-" so they can be changed into the chosen letters
def guessFill():
    global guesses
    global word
    global j

    guesses = list(range(len(word)))
    for j in range(len(word)):
        guesses[j] = "-"

# function for checking if the letter the user typed is part of the word
def guessLoop(guess):
    global word
    global i
    global j
    global k
    global count
    global letters

    for j in range(len(letters)):
        if guess == letters[j]:
            guesses[j] = guess
            count -= 1
            print("You guessed!")
            for i in guesses:
                print(i, end="")
            print()
    print(f"Letters left to guess: {count}")
    print()


# choosing a difficulty
diff = input("Enter a difficulty(easy, normal, hard): ").lower()

# easy difficulty
if diff == "easy":
    print()
    print("You have chosen the easy difficulty!")
    print("*********************************")
    print("You have the right of 10 mistakes! After that the game ends!")
    pyautogui.countdown(0)
    print()

    wordGen(easy)

    # a counter for the guessed letters
    count = len(word)

    # printing the word using only a "-" symbol
    printWord()

    # filling up a list with "-" so they can be changed into the chosen letters
    guessFill()

    # a while loop for the user to guess the word
    while count > 0:
        guess = input("Enter a guess: ")
        guessLoop(guess)

    print(f"Congratulations! You guessed the word '{word}'")

# normal difficulty
elif diff == "normal":
    print("You have chosen the normal difficulty!")
    print("*********************************")
    print("You have the right of 7 mistakes! After that the game ends!")
    pyautogui.countdown(3)
    print()

    wordGen(mid)

    # a counter for the guessed letters
    count = len(letters)

    # printing the word using only a "-" symbol
    printWord()

    # filling up a list with "-" so they can be changed into the chosen letters
    guessFill()

    # a while loop for the user to guess the word
    while count != 0:
        guess = input("Enter a guess: ")
        guessLoop(guess)

    print(f"Congratulations! You guessed the word '{word}'")


# hard difficulty
elif diff == "hard":
    print("You have chosen the hard difficulty!")
    print("*********************************")
    print("You have the right of 4 mistakes! After that the game ends!")
    pyautogui.countdown(3)
    print()

    wordGen(hard)

    # a counter for the guessed letters
    count = len(letters)

    # printing the word using only a "-" symbol
    printWord()

    # filling up a list with "-" so they can be changed into the chosen letters
    guessFill()

    # a while loop for the user to guess the word
    while count != 0:
        guess = input("Enter a guess: ")
        guessLoop(guess)

    print(f"Congratulations! You guessed the word '{word}'")


