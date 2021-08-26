import sys

from numpy.random import randn, rand
from numpy import eye
from time import time
from cardsol.problem.constraints import LinearConstraint
from cardsol.problem.functions import QuadraticForm
from cardsol.problem.model import QPModel
from cardsol.problem.objective import QPObjective
from cardsol.problem.variables import Variable
from cardsol.solver.outer_lpnlp.solver import CCQPSolver, LPNLPCCQPSolver


def cardsol_solver(n):
    k = int(n / 2)
    m = 1
    maxiter = 100

    Q = 10 * rand(n, n)
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

    start_single = time()
    obj_2 = single_tree.solve(k, m)
    end_single = time() - start_single

    start_multiple = time()
    _, obj_1 = multiple_tree.solve(k, m, maxiter)
    end_multiple = time() - start_multiple

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
    print()


if __name__ == '__main__':
    n = int(sys.argv[1])
    cardsol_solver(n)
