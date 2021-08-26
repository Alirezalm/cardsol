from gurobipy.gurobipy import GRB
from numpy.core.multiarray import ndarray
import gurobipy as gp
from cardsol.solver.abstract_solver import IMasterSolver


class GurobiOA(IMasterSolver):
    def solve(self, cutpool, fixed_continuous: ndarray, k, m):

        n = fixed_continuous.shape[0]
        num_cut = len(cutpool.pool)
        model = gp.Model("master")
        alpha = model.addMVar(shape = 1, lb = -GRB.INFINITY)
        x = model.addMVar(shape = n, lb = -GRB.INFINITY)
        delta = model.addMVar(shape = n, vtype = GRB.BINARY)

        model.setObjective(alpha, GRB.MINIMIZE)

        for cut in cutpool.pool:
            model.addConstr(alpha >= cut['fx'] + cut['gx'].T @ x - cut['gx'].T @ cut['x'])
        for i in range(n):
            model.addConstr(x[i] <= m * delta[i], name = f'{i}')
            model.addConstr(-m * delta[i] <= x[i], name = f'{i}s')
        model.addConstr(delta.sum() <= k, name = 'delta')
        model.setParam('OutputFlag', 0)
        model.optimize()

        return delta.x.reshape(n, 1), model.objval
