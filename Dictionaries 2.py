n = int(input())
mydict = {}
for i in range(n):
    line = input().split()
    mydict[line[0]] = line[1]
    
while True:
    name = input()
    
    if name == "":
        break
    else:
        if name in [i for i in mydict]:
            print(name+ "="+ mydict[name])
        else:
            print('Not found')
