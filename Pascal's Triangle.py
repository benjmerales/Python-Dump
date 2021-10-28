N = int(input("Enter N: "))
cnt = 0
prev_line = [1]
spaces = N
while cnt < N:
    line = [1]
    for i in range(cnt):
        if i == cnt-1:
            line.append(1)
        else:
            line.append(prev_line[i]+prev_line[i+1])

    for i in range(spaces):
        print("  ",end="")
    spaces -= 1
    for i in line:
        print(i," ", end="")
    print()
    prev_line = line
    cnt += 1
    
