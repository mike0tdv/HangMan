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
guessed = False
countRight = 0
countFalse = 0
countRight1 = 0
letters = []
word = []
def wordGen(x):
    rnd = random.randint(0, 4)
    letters = list(words[x][rnd])
    print("This is your word: ")
    for i in range(len(letters)):
        word.append("_")
        print(word[i], end="")

def letterCheck(y, x, z, x1):
    for i in range(len(letters)):
        if letters[i] == y:
            word[i] = y
            x1 = x + 1
    if x1 == x:
        z += 1
    else:
        x = x1

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
        else:
            print("There is no such difficulty!")

    while diffEasy:
        playAgain = False
        print("You have the right for 10 mistakes. After this the game ends!")
        print("The game will now choose a word...")
        pyautogui.countdown(1)
        print()
        wordGen(0)
        print()
        diffEasy = False

        while not guessed:
            diffEasy = False
            guess = input("Give your guess: ")
            # letterCheck(guess, countRight, countRight1, countFalse)
            for i in range(len(letters)):
                if letters[i] == guess:
                    word[i] = guess
                    countRight1 = countRight + 1
            # if countRight1 == countRight:
            #     countFalse += 1
            else:
                countRight = countRight1

            for i in range(len(letters)):
                print(word[i], end="")

            if countRight == len(letters) + 1:
                guessed = True
                print("You Win!")
                pa = (input("Do you want to play again(True/False): ")).lower()
                if pa == "true":
                    playAgain = True
                break
            elif countFalse == 10:
                guessed = True
                print("You lose!")
                pa = (input("Do you want to play again(True/False): ")).lower()
                if pa == "true":
                    playAgain = True
                break

