N = int(input("Enter Size: "))

for i in range(N):
    for j in range(N):
        print(i,j, end='\t')
    print("\n")

mid = (N - 1) // 2
X, Y = -mid, -mid
print("\n\n")

for i in range(N):
    for j in range(N):
        print(X, Y, end='\t')
        Y += 1
    print("\n")
    Y = -mid
    X += 1
