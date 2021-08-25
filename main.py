from numpy import array
from numpy.random import randn
from numpy import eye
from problem.constraints import LinearConstraint
from problem.functions import QuadraticForm, AffineForm
from problem.model import QPModel
from problem.objective import QPObjective
from problem.variables import Variable
from solver.outerapproximation.primal import QPPrimalSolver
from solver.outerapproximation.solver import CCQPSolver

n = 3

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

delta = array([1, 0, 1]).reshape(n, 1)
for i in range(n):
    d = - m * delta[i]
    const_func = AffineForm(A[i, :], d, x)
    constr.add_constr(const_func)
    const_func = AffineForm(-A[i, :], d, x)
    constr.add_constr(const_func)

model = QPModel(objective, constr)

solver = CCQPSolver(model)

solver.solve(3, 1, 100)
