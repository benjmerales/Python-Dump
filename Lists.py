if __name__ == '__main__':
    N = int(input())
    inputs = []
    for _ in range(N):
        inputs.append(input().split())

    list = []
    for line in inputs:
        a = line[0]
        
        if a == "insert":
            list.insert(int(line[1]), int(line[2]))
        elif a == "print":
            print(list)
        elif a == "remove":
            list.remove(int(line[1]))
        elif a == "append":
            list.append(int(line[1]))
        elif a == "sort":
            list.sort()
        elif a == "pop":
            list.pop()
        elif a == "reverse":
            list.reverse()
        
