import math
number = int(input("Enter a number: "))

def isPerfectSquare(number):
    if(number <= 0):
        return False
    r = int(math.sqrt(number))
    if r * r == number:
        return True
    else:
         return False

def isFibo(number):
    return isPerfectSquare((5 * number * number) + 4) or isPerfectSquare((5 * number * number) - 4)

def checkIfFibo(number):
    if( number <= 1):
        return number
    return checkIfFibo(number) + checkIfFibo(number - 1)
for i in range(1, number):
    print(i, "is a Fibonacci Number: ", isFibo(i))