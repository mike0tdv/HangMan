import random
import pyautogui

fraudWords = ["log", "word", "phone", "board", "mouse"]
midWords = ["block", "poster", "lumber", "marker", "blanket"]
HimWords = ["keyboard", "parliament", "ministry", "infrastructure", "internal"]

words = [fraudWords, midWords, HimWords]

diffEasy = False
diffMid = False
diffHard = False
diffFalse = True
letters = []
def wordGen(x):
    rnd = random.randint(0, 4)
    letters = list(words[x][rnd])
    print("This is your word: ")
    for i in range(len(letters)):
        print("_", end="")




playAgain = True
while playAgain:

    print("This is a Hang-Man game!")
    print("Choose a difficulty between the following: Easy, Medium, Hard")

    while diffFalse:
        diff = (input("Choose your difficulty: ")).lower()

        if diff == "easy":
            diffEasy = True
            break
        elif diff == "medium":
            diffMid = True
            break
        elif diff == "hard":
            diffHard = True
            break
        else: print("There is no such difficulty!")

    while diffEasy == True:
        playAgain = False
        diffEasy = False
        print("You have thr right for 10 mistakes. After this the game ends!")
        print("The game will now choose a word...")
        pyautogui.countdown(3)
        print()
        wordGen(0)
