# Hangman v1.0
#      ------\
#      |     |
#    (o_o)   |
#   /[   ]\  |
#    /   \   |
#           ===
# Simple command-line hangman game with randomly generated word from list created by me.

import wordGenerator
import time

# game variables
word = wordGenerator.gen()  # randomly-generated word
win = False                 # True if player wins
attempts = 0                # number of failed attempts, if 6, player loses
user = ""                   # string input given from letters guessed
guesses = ""                # string holding all characters that the user has guessed
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

# checkFullWord
# iterates through secret word and verifies that letter is in guesses,
# if all letters are found in guesses, then returns true
def checkFullWord():
    for c in word:
        if checkForLetter(guesses, c) == False:
            return False # at least 1 letter does not exist, so player has not won yet
    return True # no error found, return True

# printStatus
# prints out the current state of guessed word with pool of guessed
# letters following
def printStatus():
    for s in hangmans[attempts]:    # print the status of the hangman
        print(s)
    for c in word.lower():  # print the secret word with guessed letters filled in
        if checkForLetter(guesses,c) == True:
            print(c, end = " ")
        else:
            print("_", end = " ")
    print("")
    if(len(guesses)>0):     # print all letters incorrectly guessed
        print("Pool:", end = " ")
        for c in guesses.lower():
            if checkForLetter(word,c) == False:
                print(c, end = " ")
        print("")

# output prompt
print("============================")
print("Let's play hangman!")
print("============================")
print("Guess a letter or the word when you're ready!")
print("To quit anytime, just enter 'quit()'")
print("--")

# run game until 'quit()' or loss or win
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
            if checkForLetter(guesses, user) == False:  # avoid duplicate inputs
                guesses+=user
                if checkForLetter(word, user) == True:
                    if checkFullWord() == True:
                        win = True
                        break
                    print("Yes!")
                    time.sleep(1)
                else:
                    attempts+=1
                    if(attempts==6): break
                    print("Try again!")
                    time.sleep(1)
            else:
                if checkForLetter(word, user) == True:
                    print("Correct, but you guessed this already!")
                    time.sleep(1)
                else:
                    attempts+=1
                    if(attempts==6): break
                    print("Careful!  You already guessed this wrong letter!")
                    time.sleep(1)
        print("")
    printStatus()
    user = input("> ")

# final print
if win == True:
    print("")
    for s in hangmans[7]:   # print hangman (win emote)
        print(s)
    for c in word:          # print revealed secret word
        print(c, end=" ")
    print("")
    print("Hooray!  Thanks for playing!")
else:
    print("")
    for s in hangmans[6]:   # print hangman (loss emote)
        print(s)
    for c in word:          # print revealed secret word
        print(c, end=" ")
    print("")
    print("Better luck next time.  Thanks for playing!")
