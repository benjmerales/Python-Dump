# using list
opstack = []
output = []
string =  "1 + 2 + 3 + 4".split(' ')
print(string)
for i in string:
	if i == '+' or i == '-'or i == '*' or i == '/':
		opstack.append(i)
	elif i == '(':
		opstack.push(i)
	elif i == ')':
		opstack.pop()