# Find GCD
#x = int(input("Enter First Number: "))
#y = int(input("Enter Second Number: "))
x = 10
y = 20
while True:
	lowest, highest = min(x,y), max(x,y)
	remain = highest % lowest
	print(remain)
	if remain == 0:
		print("GCD: ", lowest)
		break
	highest, lowest = lowest, remain 