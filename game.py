# Hangman v1
#      ------\
#      |     |
#    (o_o)   |
#   /[   ]\  |
#    /   \   |
#           ===
# Simple command-line hangman game with randomly generated word from list created by me.
#    ~ ------\
# ~      '   |
# '   `   `  |'
#   \(^O^)/  |
#    [   ]   |
#    /   \  ===


import wordGenerator
import time

# game variables
word = wordGenerator.gen()
win = False
attempts = 0
user = ""
guesses = ""
hangmans = [
    [
        "       ------\ ",
        "       |     |",
        "             |",
        "             |",
        "             |",
        "            ==="
    ],
    [
        "       ------\ ",
        "       |     |",
        "     (o_o)   |",
        "             |",
        "             |",
        "            ==="
    ],
    [
        "       ------\ ",
        "       |     |",
        "     (o_o)   |",
        "     [   ]   |",
        "             |",
        "            ==="
    ],
    [
        "       ------\ ",
        "       |     |",
        "     (o_o)   |",
        "    /[   ]   |",
        "             |",
        "            ==="
    ],
    [
        "       ------\ ",
        "       |     |",
        "     (o_o)   |",
        "    /[   ]\  |",
        "             |",
        "            ==="
    ],
    [
        "       ------\ ",
        "       |     |",
        "     (o_o)   |",
        "    /[   ]\  |",
        "     /       |",
        "            ==="
    ],
    [
        "       ------\ ",
        "       |     |",
        "     (x_x)   |",
        "    /[   ]\  |",
        "     /   \   |",
        "            ==="
    ],
    [
        "     ~ ------\ ",
        "  ~      '   |",
        "  '   `   `  |'",
        "    \(^O^)/  |",
        "     [   ]   |",
        "     /   \  ==="
    ]
]

# checkForLetter
# iterates through 'w' to check if the letter 'char' exists
# returns true if exists, else false
def checkForLetter(w, char):
    for c in w.lower():
        if c == char.lower():
            return True
    return False

# printStatus
# prints out the current state of guessed word with pool of guessed
# letters following
def printStatus():
    for s in hangmans[attempts]:
        print(s)
    for c in word.lower():
        if checkForLetter(guesses,c) == True:
            print(c, end = " ")
        else:
            print("_", end = " ")
    print("")
    if(len(guesses)>0):
        print("Pool:", end = " ")
        for c in guesses.lower():
            if checkForLetter(word,c) == False:
                print(c, end = " ")
        print("")

# output prompt
print("")
print("============================")
print("Let's play hangman!")
print("============================")
print("Guess a letter or the word when you're ready!")
print("To quit anytime, just enter 'quit()'")
print("--")

while user != "quit()":
    if user != "":
        if len(user)>1:
            if(user.lower()==word.lower()):
                print("")
                win = True 
                break
            else:
                attempts+=1
                if(attempts==6): break
                print("Not quite!")
                time.sleep(1)
        else:
            guesses+=user
            if checkForLetter(word, user) == True:
                print("Correct!")
                time.sleep(1)
            else:
                attempts+=1
                if(attempts==6): break
                print("Try again!")
                time.sleep(1)
        print("")
    printStatus()
    user = input("> ")

if win == True:
    print("")
    for s in hangmans[7]:
        print(s)
    for c in word:
        print(c, end=" ")
    print("")
    print("Hooray!  Thanks for playing!")
else:
    print("")
    for s in hangmans[6]:
        print(s)
    for c in word:
        print(c, end=" ")
    print("")
    print("Better luck next time.  Thanks for playing!")
