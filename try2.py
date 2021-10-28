n = int(input())
l = []
for _ in range(n):
    l.append(input())

for i in l:
    if i[0] == '7' or i[0] == '8' or i[0] == '9':
        print('YES')
    else:
        print('NO') 
