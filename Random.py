import random
import time
from datetime import datetime

def RandomA():
    print(random.randrange(0,10), end='\t') # Random integer [start, stop, step]
    # doesn't include endpoint
def RandomB():
    print(random.randint(0,10), end='\t')   # Random integer that includes points
    
def RandomC():
    #using seeds
    thiseed = datetime.now()
    random.seed(thiseed)
    print("Seed is ", thiseed)
    print("First Call Number: ", random.randint(25,50))
    print("Second Call Diff Res: ", random.randint(25,50))
    random.seed(thiseed)
    print("Third Call that Initializes same Seed: ", random.randint(25,50))
    print()

def RandomD():
    #Sequences
    list = ["alpaca", "boar", "chicken", "deer", "elephant", "fly", "giraffe", "hornet",
            "iguana", "jaguar", "kiwi", "leopard", "moose", "neko", "owl", "parrot",
            "quail", "rabbit", "snake", "turtle", "ulod", "vulture", "worm", "X", "zebra"]
    print(random.choice(list), end='\t')

def RandomE():
    # Sequences with frequency
    list = ["apple", "banana", "cherry", "durian", "eggplant"]
    print(random.choices(list, [1,2,3,4,5], k = 5))

def RandomF():
    # Samples ( Sequences without replacements )
    list = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    print(random.sample(list, 4))
    
while True:
    RandomF()
    time.sleep(0.5)
    
