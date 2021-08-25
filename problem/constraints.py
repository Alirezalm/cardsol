from typing import List

from problem.abstract_classes import IConstraint, IFunction
from problem.functions import AffineForm


class LinearConstraint(IConstraint):
    def __init__(self, constr: List[AffineForm] = []):
        self.constr_list = constr

    def add_constr(self, const_func: AffineForm):
        self.constr_list.append(const_func)
