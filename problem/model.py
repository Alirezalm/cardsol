from problem.abstract_classes import IObjective, IConstraint


class Model:
    def __init__(self, objective: IObjective, constraints: IConstraint):
        self.objective = objective
        self.constraints = constraints

