s = "aQ2"
res = False
bolist = [False,False,False,False,False]
for i in s:
	if i.isalnum():
		bolist[0] = True
	if i.isalpha():
		bolist[1] = True
	if i.isdigit():
		bolist[2] = True
	if i.islower():
		bolist[3] = True
	if i.isupper():
		bolist[4] = True

for b in bolist:
	print(b)