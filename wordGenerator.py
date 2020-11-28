import random

words = [
    "apple",
    "banana",
    "coconut",
    "diamond"
]

def gen(): 
    r = random.randrange(0,len(words),1)
    return words[r]