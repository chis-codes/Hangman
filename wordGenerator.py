# wordGenerator.py
# module for returning a random word to caller using function gen()

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