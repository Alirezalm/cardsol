from numpy import zeros
from cardsol.problem.model import QPModel
from cardsol.solver.outer_lpnlp.master import MasterSolverManager
from cardsol.solver.outer_lpnlp.primal import QPPrimalSolver
from cardsol.solver.subsolvers.gurobilpnlp import GurobiLPNLPBBSolver
import click
import subprocess

subprocess.run("clear")


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
        # click.secho("oa cut added to master problem\n".upper(), fg = 'green')

    def get_pool(self):
        # click.secho("generating cuts\n".upper(), fg = 'green')
        return self.pool


class AlgorithmController:
    def __init__(self, tol = 1e-8, upper = 1e4, lower = -1e4):
        click.secho("initialization\n".upper(), fg = 'green')
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
        # click.secho("updating upper bound \n".upper(), fg = 'green')
        self.upper_list.append(up)

    @property
    def last_lower(self):
        return self.lower_list[-1]

    @last_lower.setter
    def last_lower(self, lb):
        # click.secho("updating lower bound \n".upper(), fg = 'green')
        self.lower_list.append(lb)

    def error(self):
        return self.last_upper - self.last_lower

    def is_terminated(self):
        if self.error() <= self.tol:
            click.secho("outer approximation terminated successfully".upper(), fg = 'green')
            return True
        else:
            return False

    def display(self, k):

        click.secho(f"{k:3}       {self.last_upper:3.5f}       {self.last_lower:3.5f}       {self.error():3.5f}", fg = "blue")


class CCQPSolver:
    click.secho("""
    
                                       cardsol: cardinality constrained optimization solver
                                       
    """.upper(), fg = 'blue', bold = True)

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
        kiter = 0
        click.secho("=============== cardsol started =============== \n".upper(), fg = 'green')
        click.secho("iter           up          lb          error", fg = "blue")
        while (not algorithm_manager.is_terminated()) & (kiter <= maxiter):
            kiter += 1
            x, upper_bound = primal_solver.solve(model = self.model, fixed_binary = delta, m_bound = m)
            cut_manager.add_cut(upper_bound, gx = self.model.objective.get_grad(x), x = x)
            delta, lower_bound = master_solver.solve(cut_manager, x, k, m)

            algorithm_manager.last_upper = min(algorithm_manager.last_upper, upper_bound)
            algorithm_manager.last_lower = lower_bound
            algorithm_manager.display(kiter)

        return x, algorithm_manager.last_upper


class LPNLPCCQPSolver:
    def __init__(self, model: QPModel):
        self.model = model
        self.n = self.model.objective.func.x.shape[0]

    def solve(self, k: int, m: float):
        click.secho("""

                                          lp/nlp based branch and cut method is started (single tree oa)

        """.upper(), fg = 'green', bold = True)
        solver = GurobiLPNLPBBSolver()
        obj = solver.solve(k, m, self.n, self.model)
        return obj
