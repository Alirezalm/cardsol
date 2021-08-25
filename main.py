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

n = 5

Q = randn(n, n)
Q = Q + Q.T
Q = Q.T @ Q
c = randn(n, 1)

A = eye(n, n)

m = 1
x = Variable(shape = (n, 1), name = "x")

obj_func = QuadraticForm(Q, c, x)

objective = QPObjective(obj_func, sense = "minimize")

constr = LinearConstraint()


for i in range(n):
    d = - m
    const_func = AffineForm(A[i, :], d, x)
    constr.add_constr(const_func)
    const_func = AffineForm(-A[i, :], d, x)
    constr.add_constr(const_func)

model = QPModel(objective, constr)

solver1 = CCQPSolver(model)

solver = LPNLPCCQPSolver(model)

k = 2
m = 0.5
maxiter = 100
solver1.solve(k, m, 100)
solver.solve(k, m)
# print(x, obj)