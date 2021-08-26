from cardsol.problem.abstract_classes import IModel
from cardsol.problem.constraints import LinearConstraint
from cardsol.problem.objective import QPObjective


class QPModel(IModel):

    def __init__(self, objective: QPObjective, constraints: LinearConstraint):

        self.objective = objective
        self.constraints = constraints
