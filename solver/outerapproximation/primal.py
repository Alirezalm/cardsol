from numpy import ndarray
from problem.model import QPModel
from solver.abstract_solver import IPrimalSolver
from solver.subsolvers.gurobi_qp import GurobiQPSolver


class QPPrimalSolver(IPrimalSolver):
    def __init__(self):
        solution = {}

    def solve(self, model: QPModel, fixed_binary: ndarray, m_bound):
        solver = GurobiQPSolver()
        sol, obj = solver.solve(model, fixed_binary, m_bound)
        return sol, obj
