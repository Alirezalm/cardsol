from typing import List

from problem.abstract_classes import IConstraint, IFunction


class Constraint(IConstraint):
    def __init__(self, constr: List[IFunction] = []):
        self.constr = constr

    def add_constr(self, const_func: IFunction):
        self.constr.append(const_func)
