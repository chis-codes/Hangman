import wordGenerator

# checkForLetter
# iterates through 'word' to check if the letter 'char' exists
# returns true if exists, else false
def checkForLetter(word, char):
    for c in word.lower():
        if c == char.lower():
            return True
    return False

print(wordGenerator.gen())