X = int(input("Enter number: "))

def Factorial(X):
    if X == 1:
        return 1
    else:
        return X * Factorial(X-1)
    
print("Factorial: ", Factorial(X))
