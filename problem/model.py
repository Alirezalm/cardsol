from problem.abstract_classes import IObjective, IConstraint, IModel
from problem.constraints import LinearConstraint
from problem.objective import QPObjective


class QPModel(IModel):

    def __init__(self, objective: QPObjective, constraints: LinearConstraint):
        self.objective = objective
        self.constraints = constraints
