from numpy import zeros
from problem.model import QPModel
from solver.outerapproximation.master import MasterSolverManager
from solver.outerapproximation.primal import QPPrimalSolver
from solver.subsolvers.gurobilpnlp import GurobiLPNLPBBSolver


class CutManager:
    def __init__(self):
        self.pool = []

    def add_cut(self, fx, gx, x):
        cut_info = {
            "fx": fx,
            "gx": gx,
            "x": x
        }
        self.pool.append(cut_info)

    def get_pool(self):
        return self.pool


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

    def error(self):
        return self.last_upper - self.last_lower

    def is_terminated(self):
        if self.error() <= self.tol:
            return True
        else:
            return False

    def display(self):
        print(f"up: {self.last_upper} lb: {self.last_lower} error: {self.error()}")


class CCQPSolver:
    def __init__(self, model: QPModel):
        self.model = model

    def solve(self, k: int, m: float, maxiter = 100):
        algorithm_manager = AlgorithmController()
        primal_solver = QPPrimalSolver()
        master_solver = MasterSolverManager()
        cut_manager = CutManager()
        n = self.model.objective.func.x.shape[0]
        delta = zeros((n, 1))
        x = None
        upper_bound = None
        while not algorithm_manager.is_terminated():
            x, upper_bound = primal_solver.solve(model = self.model, fixed_binary = delta, m_bound = m)
            cut_manager.add_cut(upper_bound, gx = self.model.objective.get_grad(x), x = x)
            delta, lower_bound = master_solver.solve(cut_manager, x, k, m)

            algorithm_manager.last_upper = min(algorithm_manager.last_upper, upper_bound)
            algorithm_manager.last_lower = lower_bound
            algorithm_manager.display()

        return x, upper_bound


class LPNLPCCQPSolver:
    def __init__(self, model: QPModel):
        self.model = model
        self.n = self.model.objective.func.x.shape[0]

    def solve(self, k: int, m: float):
        solver = GurobiLPNLPBBSolver()
        solver.solve(k, m, self.n, self.model)
