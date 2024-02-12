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
mistakes = 0
mistakes1 = 0

word = ""
letters = []
rnd = 0
i = ""
j = 0
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

def guessFill():
    global guesses
    global word
    global j
    guesses = list(range(len(word)))
    for j in range(len(word)):
        guesses[j] = "-"

# choosing a difficulty
diff = input("Enter a difficulty(easy, normal, hard): ").lower()

# easy difficulty
if diff == "easy":
    print()
    print("You have chosen the easy difficulty!")
    print("*********************************")
    print("You have the right of 10 mistakes! After that the game ends!")
    pyautogui.countdown(3)
    print()

    wordGen(easy)

    # making a counter for the guessed letters
    count = len(letters)
    # rnd = random.randint(0, 4)
    # word = words[y][rnd]
    # letters = list(word)

    # printing the word using only a "-" symbol
    printWord()
    # for i in word:
    #     print("-", end="")
    # print()

    # filling up a list with "-" so they can be changed into the chosen letters
    guesses = list(range(len(word)))
    for i in range(len(word)):
        guesses[i] = "-"

    # a while loop for the user to guess the word
    while count != 0:
        guess = input("Enter a guess: ")

        for i in range(len(word)):
            if guess == word[i]:
                count -= 1
                guesses[i] = guess
                print("You guessed!")
                for j in guesses:
                    print(j, end="")
            else:
                mistakes1 += 1
        print()
        print(f"Letters to be guessed left: {count} ")
        # print(f"Mistakes left: {mistakes1}")
        print()
        # if mistakes1 > mistakes:
        #     mistakes = mistakes1
        #     for j in guesses:
        #         print(j, end="")
        # print()
    print(f"Congratulations! You guessed the word '{word}'")

# normal difficulty
elif diff == "normal":
    print("You have chosen the normal difficulty!")

# hard difficulty
elif diff == "hard":
    print("You have chosen the hard difficulty!")

