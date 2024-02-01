import threading
import pyautogui

fraudWords = ["log", "word", "phone", "board", "mouse"]
midWords = ["block", "poster", "lumber", "marker", "blanket"]
HimWords = ["keyboard", "parliament", "ministry", "infrastructure", "internal"]


playAgain = True
while playAgain:
    print("This is a Hang-Man game!")
    print("Choose a difficulty between the following: Easy, Medium, Hard")
    diff = (input("Choose your difficulty: ")).lower()

    while diff == "easy":
        print("You have thr right for 10 mistakes. After this the game ends!")
        print("The game will now choose a word...")
        pyautogui.countdown(5)
