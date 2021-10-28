if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    max_num = 0
    for i in arr:
        if max_num < i:
            max_num = i

    second = 0
    
    for i in arr:
        if max_num == i:
            continue

        if second < i:
            second = i


    print(second)
     
