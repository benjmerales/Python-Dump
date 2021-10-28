def getCorrectInput(inputs):
    inp = input("Enter Input: ")
    while inp not in inputs:
        print("!Input Error: Please select a valid input")
        inp = input("Enter Input: ")
    return inp

def getCorrectIncome(text):
    while True:
        try:
            x = int(input(text))
        except ValueError:
            print("!Value Error: Please enter a valid MGI")
            continue

        if x <= 0:
            print("!Value Error: Please enter a positive MGI")
            continue
        break
    return x

def getSSSPayment(income):
    # for private only
    intervals = (0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000)
    payment = ( 150, 175, 200, 225, 250, 275, 300, 325, 350, 375) 
    i = 1
    while i < len(intervals):
        if intervals[i-1] < income and intervals[i] > income:
            return payment[i-1]
        i += 1
    return -1

def getGSISPayment(income):
    # GSIS is for government only
    return income * 0.09

def getPIPayment(income):
    # For both government and Private (2021 Basis)
    if income <= 1500:
        return income * 0.01
    else:
        return income * 0.02

def getPHPayment(income):
    # For both Government and Private (2022 Basis)
    if income <= 10000:
        return 400
    elif income > 10000 and income < 70000:
        return income * 0.035
    else:
        return 2450 

def computeIncome(my_income, spouse_income):
    print("Is over Php90000?", end='')
    if(my_income > 90000): print("Yes")
    else: print("No")

    income = my_income + spouse_income
    print("Net Pay after Tax: ")
    print("Total Monthly Contribution: ")
    # Print the payments using functions

def main():
    print("Tax Calculator (2023)")

    print("Civil Status?")
    print("\tA.) Single")
    print("\tB.) Married")

    cv = getCorrectInput(['A', 'a', 'B', 'b'])

    print("Your Job Sector?")
    print("\tA.) Private")
    print("\tB.) Government")
    print("\tC.) Overseas Foreign Worker (OFW)")

    js = getCorrectInput(['A', 'a', 'B', 'b','C','c'])
    mgi = getCorrectIncome("Enter Monthly Gross Income: ")

    if cv == 'B' or cv == 'b':
        print("Your Spouse's Job Sector?")
        print("\tA.) Private")
        print("\tB.) Government")
        print("\tC.) Overseas Foreign Worker (OFW)")
        s_js =  getCorrectInput(['A', 'a', 'B', 'b','C','c'])
        s_mgi = getCorrectIncome("Enter Spouse's MGI: ")

    print("Results: ")

