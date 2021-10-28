from sympy import *
import math

x = Symbol('x')

f = x * (math.e**x)
print(f)
f_prime = f.diff(x)
print(f_prime)
