arr = [2,3,4,1,5]
swaps = 0
def swap(i1, i2):
	arr[i1], arr[i2] = arr[i2], arr[i1]

def check():
	for i in range(len(arr)-1):
		if arr[i] < arr[i+1]:
			continue
		else:
			return False
	return True

i = 0
while True:
	L = arr[i::]
	m = min(L)
	swap(i,arr.index(m))
	swaps+=1
	if check():
		print("Minimum number of swaps: ", swaps)
		exit()
	
	i+=1