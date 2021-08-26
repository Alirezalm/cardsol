from cardsol.problem.abstract_classes import IFunction, IVariable

from numpy import ndarray


class QuadraticForm(IFunction):

    def __init__(self, Q: ndarray, c: ndarray, x: IVariable):
        self.Q = Q
        self.c = c
        self.x = x

    def evaluate_at(self, x0: ndarray):
        return 0.5 * x0.T @ self.Q @ x0 + self.c.T @ x0

    def gradient_at(self, x0: ndarray):
        return self.Q @ x0 + self.c

    def hessian_at(self, x0: ndarray):
        return self.Q


class AffineForm(IFunction):
    def __init__(self, c: ndarray, d: float, x: IVariable):
        self.c = c
        self.d = d
        self.x = x

    def evaluate_at(self, x0):
        return self.c.T @ x0 + self.d

    def gradient_at(self, x0 = None):
        return self.c

    def hessian_at(self, x0 = None):
        return 0.0
