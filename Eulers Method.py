from sympy import *
import math
x, y = symbols('x y')
step_x = [1,2,3,4,5,6,7,8,9,10]
h = [0.1, 0.05, 0.025]
xi = 1
yi = 1

f = -  (y**2)
f_xyA = yi
f_xyB = yi
f_xyC = yi

solution = 1/x
s_x = lambdify(x, solution)
print("f(x,y) = ", f)
print("x \t\t h=0.1 \t\t\t\t\t h=0.05 \t\t h = 0.025 \t\t\t Exact")
for i in range(len(step_x)):
    print(step_x[i], end = "\t\t")

    eulersA = f_xyA + h[0] * f.subs([(x, step_x[i]), (y,f_xyA)])
    f_xyA = eulersA
    print(eulersA, end="\t\t")

    eulersB = f_xyB + h[1] * f.subs([(x, step_x[i]), (y,f_xyB)])
    f_xyB = eulersB
    print(eulersB, end="\t\t")

    eulersC = f_xyC + h[2] * f.subs([(x, step_x[i]), (y,f_xyC)])
    f_xyC = eulersC
    print(eulersC, end="\t\t")

    print(s_x(step_x[i]))
