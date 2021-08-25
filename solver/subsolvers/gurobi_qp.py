from gurobipy.gurobipy import GRB
from numpy import ndarray

from problem.model import QPModel
from solver.abstract_solver import IPrimalSolver
import gurobipy as gp


class GurobiQPSolver(IPrimalSolver):

    def solve(self, model: QPModel, fixed_binary: ndarray = None):
        m = gp.Model("qp")

        n = model.objective.func.x.shape[0]
        isinteger = model.objective.func.x.integer
        n_const = len(model.constraints.constr_list)
        x = m.addMVar(shape = n, lb = -GRB.INFINITY)

        obj = x @ model.objective.func.Q @ x + model.objective.func.c.T @ x

        sense = None

        if model.objective.sense == "minimize":
            sense = GRB.MINIMIZE
        else:
            sense = GRB.MAXIMIZE

        m.setObjective(obj, sense)
        for i in range(n_const):
            const = model.constraints.constr_list[i].c.T @ x + model.constraints.constr_list[i].d
            m.addConstr(const <= 0)

        m.optimize()
        print(x.x , m.objval)
        return x.x , m.objval