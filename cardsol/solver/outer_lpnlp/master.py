from cardsol.solver.subsolvers.gurobiOA import GurobiOA


class MasterSolverManager:
    @staticmethod
    def solve(cutpool, x, k, m):
        solver = GurobiOA()
        delta, obj = solver.solve(cutpool, x, k, m)
        return delta, obj