year = int(input("Enter a Year"))

if year <=0 :
    print("Input a valid year!")
if year % 4 == 0:
    print(year, " is a leap year")
else:
    print(year, " is NOT a leap year")