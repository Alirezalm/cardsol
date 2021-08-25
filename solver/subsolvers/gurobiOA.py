from numpy.core.multiarray import ndarray

from problem.abstract_classes import IModel
from solver.abstract_solver import IMasterSolver


class GurobiOA(IMasterSolver):
    def solve(self, model: IModel, fixed_continuous: ndarray):
        pass
