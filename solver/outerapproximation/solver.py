from numpy import zeros

from problem.model import QPModel
from solver.outerapproximation.primal import QPPrimalSolver


class AlgorithmController:
    def __init__(self, tol = 1e-3, upper = 1e4, lower = -1e4):
        self.tol = tol
        self.upper = upper
        self.lower = lower
        self.upper_list = [upper]
        self.lower_list = [lower]

    @property
    def last_upper(self):
        return self.upper_list[-1]

    @last_upper.setter
    def last_upper(self, up):
        self.upper_list.append(up)

    @property
    def last_lower(self):
        return self.lower_list[-1]

    @last_lower.setter
    def last_lower(self, lb):
        self.lower_list.append(lb)

    def is_terminated(self):
        if self.last_upper - self.last_lower <= self.tol:
            return True
        else:
            return False


class CCQPSolver:
    def __init__(self, model: QPModel):
        self.model = model

    def solve(self, k: int, m: float, maxiter = 100):
        algorithm_manager = AlgorithmController()
        primal_solver = QPPrimalSolver()
        n = self.model.objective.func.x.shape[0]
        delta = zeros((n, 1))
        while not algorithm_manager.is_terminated():
            x, upper_bound = primal_solver.solve(model = self.model, fixed_binary = delta)
            break
