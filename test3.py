import numpy as np

s = np.random.uniform(0,1,5)

a = [[1,2,3],[4,5,6],[7,8,9]]
print("a", a)
print("a[0]", a[0])
print("a[:]", a[:])
print("a[0][1]", a[0][1])
print("a[1][0]", a[1][0])
print("a[:][0]", a[:][0])
print("a[0][:]", a[0][:])

print("\n~~~~~~~~~~~~~~~~~~~~~\n")

x = np.zeros((5,5))

print(x[2,:])
print(x[2][1])
