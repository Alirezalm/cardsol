from typing import Tuple
from cardsol.problem.abstract_classes import IVariable

class Variable(IVariable):
    def __init__(self, shape: Tuple = (), name: str = "", integer: bool = False):
        self.shape = shape
        self.name = name
        self.integer = integer
