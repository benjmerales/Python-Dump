from sympy import *
import math
x = Symbol('x')

f = x**3 - 9*(x**2) + 3.8197
x_i = 9

f_prime = f.diff(x)
print("f(x) = " , f)
print("f'(x) = " , f_prime)


f_x = lambdify(x, f)
f_prime_x = lambdify(x, f_prime)

#print("x0 = ", x_i)
#print(x_i)
for i in range(1,10):
    new = x_i - ( f_x(x_i) / f_prime_x(x_i) )
    #print("x"+str(i)+" = ", new)
    print(new)
    x_i = new
