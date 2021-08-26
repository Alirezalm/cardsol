import click
from gurobipy.gurobipy import GRB
import gurobipy as gp
from numpy import array
from numpy import zeros

from cardsol.problem.model import QPModel
from cardsol.solver.outer_lpnlp.primal import QPPrimalSolver


class GurobiLPNLPBBSolver:
    primal_solver = QPPrimalSolver()

    def solve(self, k, m, n, primal_model: QPModel):
        def single_tree_callback(my_model, where):
            if where == GRB.Callback.MIPSOL:
                incumbent = my_model.cbGetSolution(my_model._vars)
                incumbent = array(incumbent).reshape(-1, 1)
                fixed_bin = incumbent[1: n + 1]
                x_decision = my_model._vars[n + 1:]
                primal_solver = QPPrimalSolver()
                sol, obj = primal_solver.solve(primal_model, fixed_bin, m)
                cut = {
                    "fx": obj,
                    "gx": primal_model.objective.get_grad(sol),
                    "x": sol,
                }
                model.cbLazy(
                    cut['fx'] + sum([cut['gx'][j][0] * (x_decision[j] - sol[j]) for j in range(n)]) <= my_model._vars[
                        0])

        psolver = QPPrimalSolver()
        fixed_bin = zeros((n, 1))
        sol, obj = psolver.solve(primal_model, fixed_bin, m)

        cut = {
            "fx": obj,
            "gx": primal_model.objective.get_grad(sol),
            "x": sol,
        }

        model = gp.Model("master")
        alpha = model.addVar(lb = - GRB.INFINITY)
        # x = []
        # for i in range(n):
        #     x.append(model.addVar(lb = -GRB.INFINITY))

        # delta = model.addMVar(shape = n, vtype = GRB.BINARY)

        model.setObjective(alpha, GRB.MINIMIZE)

        # for cut in cutpool.pool:
        #     model.addConstr(alpha >= cut['fx'] + cut['gx'].T @ x - cut['gx'].T @ cut['x'])
        x = model.addVars(n, 1, lb = -GRB.INFINITY)
        delta = model.addVars(n, 1, lb = -GRB.INFINITY, vtype = GRB.BINARY)

        model.addConstr(
            cut['fx'] + sum([cut['gx'][j][0] * (x[j, 0] - sol[j]) for j in range(n)]) <= alpha)

        for i in range(n):
            model.addConstr(x[i, 0] <= m * delta[i, 0], name = f'{i}')
            model.addConstr(-m * delta[i, 0] <= x[i, 0], name = f'{i}s')
        model.addConstr(delta.sum() <= k, name = 'delta')
        # model.addConstr(alpha >= -1e4)
        model.setParam('OutputFlag', 1)
        mylist = [alpha]
        for i in range(n):
            mylist.append(delta[i, 0])
        for i in range(n):
            mylist.append(x[i, 0])
        model._vars = mylist
        model.Params.lazyConstraints = 1
        model.optimize(single_tree_callback)
        # for v in model.getVars():
        #     print(v.x)
        return model.objval
