import math
def BinarySearch (l, lwr, upr, 	C):
	if upr >= lwr:
		mid = math.floor((upr+lwr) / 2)
		print("Probing At Position:", mid)
		if l[mid] == C:
			print("Found at position ", mid)
			return True
		else:
			if(l[mid] > C):
				BinarySearch(l, lwr, mid, C)
			else:
				BinarySearch(l, mid, upr, C)
	else:
		print(C, "wasn't found...")
		return False

myList = [5,9,56,123,234,345,2356,12345,64543]

BinarySearch(myList, 0, len(myList)-1, 5)