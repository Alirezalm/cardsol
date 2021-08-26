from gurobipy.gurobipy import GRB
from numpy import ndarray

from cardsol.problem.model import QPModel
from cardsol.solver.abstract_solver import IPrimalSolver
import gurobipy as gp


class GurobiQPSolver(IPrimalSolver):

    def solve(self, model: QPModel, fixed_binary: ndarray, m_bound):
        m = gp.Model("qp")

        n = model.objective.func.x.shape[0]
        isinteger = model.objective.func.x.integer
        n_const = len(model.constraints.constr_list)
        x = m.addMVar(shape = n, lb = -GRB.INFINITY)

        obj = x @ (0.5 * model.objective.func.Q) @ x + model.objective.func.c.T @ x

        if model.objective.sense == "minimize":
            sense = GRB.MINIMIZE
        else:
            sense = GRB.MAXIMIZE

        m.setObjective(obj, sense)
        # for i in range(n_const):
        #     const = model.constraints.constr_list[i].c.T @ x + model.constraints.constr_list[i].d
        #     m.addConstr(const <= 0)
        for i in range(n):
            m.addConstr(x[i] <= m_bound * fixed_binary[i], name = f'{i}')
            m.addConstr(-m_bound * fixed_binary[i] <= x[i], name = f'{i}s')
        m.setParam('OutputFlag', 0)
        m.optimize()
        return x.x.reshape(n, 1), m.objval
