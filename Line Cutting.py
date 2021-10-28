import math
# Count how many cuts
# if person cuts more than twice it is chaotic
final = [2,1,5,3,4]
orig =  [1,2,3,4,5]
n = len(final)

def compare(l1, l2):
	if l1 is l2:
		return True
	else:
		return False

def cut(l, x):
	posx = l.index(x)
	l[posx-1], l[posx] = l[posx], l[posx-1] 

print(orig)
cut(orig,5)
print(orig)