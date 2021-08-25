from numpy import array
from numpy.random import randn
from numpy import eye
from problem.constraints import LinearConstraint
from problem.functions import QuadraticForm, AffineForm
from problem.model import QPModel
from problem.objective import QPObjective
from problem.variables import Variable
from solver.outerapproximation.primal import QPPrimalSolver
from solver.outerapproximation.solver import CCQPSolver, LPNLPCCQPSolver
from time import time

n = 5
k = 2
m = 0.5
maxiter = 100

Q = randn(n, n)
Q = Q + Q.T
Q = Q.T @ Q
c = randn(n, 1)

A = eye(n, n)

x = Variable(shape = (n, 1), name = "x")

obj_func = QuadraticForm(Q, c, x)

objective = QPObjective(obj_func, sense = "minimize")

constr = LinearConstraint()

model = QPModel(objective, constr)

multiple_tree = CCQPSolver(model)

single_tree = LPNLPCCQPSolver(model)

start_multiple = time()
_, obj_1 = multiple_tree.solve(k, m, 100)
end_multiple = time() - start_multiple

start_single = time()
obj_2 = single_tree.solve(k, m)
end_single = time() - start_single

multiple_tree_info = f"""
                MULTIPLE TREE METHOD:
                    SOLUTION TIME: {end_multiple}
                    OPTIMAL OBJ:{obj_1}
"""
single_tree_info = f"""
                SINGLE TREE METHOD:
                    SOLUTION TIME: {end_single}
                    OPTIMAL OBJ:{obj_2}
"""

print(multiple_tree_info)
print()
print(single_tree_info)
print()
print(f"SINLGE THREE METHOD IS APPROXIMATELY {int(end_multiple / end_single)} TIMES FASTER")