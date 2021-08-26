from cardsol.problem.abstract_classes import IObjective
from cardsol.problem.functions import QuadraticForm


class QPObjective(IObjective):
    def __init__(self, func: QuadraticForm, sense: str = "minimize"):
        self.func = func
        self.sense = sense

    def get_obj(self, x0):
        return self.func.evaluate_at(x0)

    def get_grad(self, x0):
        return self.func.gradient_at(x0)

    def get_hessian(self, x0):
        return self.func.hessian_at(x0)

