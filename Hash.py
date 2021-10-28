import math
from sympy import *

x = Symbol('x')

h1 = (x%7)
h2 = 2 * ((x//7) + 1)
h = h1 + h2
h = lambdify(x,h)
print(h(12))
