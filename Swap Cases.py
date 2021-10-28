string = input()
newString = ""
for i in string:
    if i.islower():
        newString += i.upper()
    else:
        newString += i.lower()

print(newString)
