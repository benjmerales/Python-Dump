string = "1 * ( 2 + 3 ) "
string = string.split()
opstack = []
output = []

for i in string:
	if i == '+' or i == '-'or i == '*' or i == '/':
		output.append(i)
	elif i == '(':
		output.append(opstack[0])
		opstack.remove(0)

for i in string:
	if i.isdigit():
		output.append(i)
print(str(output))
