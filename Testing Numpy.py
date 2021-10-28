import numpy
import solution as solution

lb = [-100] * 30
ub = [100] * 30
Positions = numpy.zeros((5, 30))
for i in range(30):
    Positions[:, i] = (numpy.random.uniform(0,1, 5) * (ub[i] - lb[i]) + lb[i] )
    
Convergence_curve = numpy.zeros(1000)
s = solution

print("Lower Bound: ", lb)
print("Upper Bound: ", ub)
print("Positions: ", Positions)
#print("Convergence Curve: ", Convergence_curve)
print("Solution: ", s)
