from sympy import *
import math
x = Symbol('x')

f = 1 / x
x_ = 1

g = f.diff(x)
h = g.diff(x)
i = h.diff(x)
j = i.diff(x)
k = j.diff(x)

f_x = lambdify(x,f)
g_x = lambdify(x,g)
h_x = lambdify(x,h)
i_x = lambdify(x,i)
j_x = lambdify(x,j)
k_x = lambdify(x,k)


print(f, '\t\t | \t\t', f_x(x_))
print(g, '\t\t | \t\t', g_x(x_))
print(h, '\t\t | \t\t', h_x(x_))
print(i, '\t\t | \t\t', i_x(x_))
print(j, '\t\t | \t\t', j_x(x_))
print(k, '\t\t | \t\t', k_x(x_))

