import random
import pyautogui

fraudWords = ["log", "word", "phone", "board", "mouse"]
midWords = ["block", "poster", "lumber", "marker", "blanket"]
HimWords = ["keyboard", "parliament", "ministry", "infrastructure", "internal"]
nums = [0, 1, 2, 3, 4]

playAgain = True
while playAgain:
    print("This is a Hang-Man game!")
    print("Choose a difficulty between the following: Easy, Medium, Hard")
    diff = (input("Choose your difficulty: ")).lower()
    randm = random.choice(nums)

    while diff == "easy":
        print("You have thr right for 10 mistakes. After this the game ends!")
        print("The game will now choose a word...")

        letters = list(fraudWords[randm])
        pyautogui.countdown(3)

        for i in range(len(letters)):
            print("_", end="")