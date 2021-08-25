from numpy.core.multiarray import ndarray

from problem.abstract_classes import IModel
from problem.model import QPModel
from solver.abstract_solver import IMasterSolver
from solver.subsolvers.gurobiOA import GurobiOA
from solver.subsolvers.gurobi_qp import GurobiQPSolver


class MasterSolverManager:
    @staticmethod
    def solve(cutpool, x, k, m):
        solver = GurobiOA()
        delta, obj = solver.solve(cutpool, x, k, m)
        return delta, obj
