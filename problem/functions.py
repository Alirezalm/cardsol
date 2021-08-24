from problem.abstract_classes import IFunction, IVariable

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
