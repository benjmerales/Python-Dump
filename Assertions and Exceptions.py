'''
temp = float(input("Temperature: "))
# Asserts will not continue the code. In other words, asserts terminate.
assert (temp >=0), "Colder than absolute zero"

# Exceptions with IOError
try:
    fh = open("testfile", "r")
    fh.write("This is my test file")
except IOError:
    print("ERROR: Can\'t find file or read data")
else:
    print("Written successfully")
    fh.close()

# Exceptions with ValueError
try:
    S = input().strip()
    print(int(S))  
except ValueError:
    print("Bad String")
else:
    print("Integer")

# Try-Finally clause
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling")
finally:
    print("This will always execute even without the else and except keyword")


level = -1
if level < 1:
    raise Exception("Sorry, no numbers below zero")
    # the code below will not execute
    print("Hello World")
'''
#User Defines Exceptions
import random
class Error(Exception):
    pass
class ValueTooSmallError(Error):
    pass
class ValueTooLargeError(Error):
    pass

number = random.randint(0,100)
tries = 0
while True:
    try:
        X = int(input("Guess a number (0-100): "))
        if X < number:
            raise ValueTooSmallError
        elif X > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Too Low \n")
    except ValueTooLargeError:
        print("Too High \n")
    finally:
        tries+=1
print("Congratulations! You Guess it Correctly!", number, "is the correct number!")
print("Number of Tries: ", tries)




















