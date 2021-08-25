from abc import ABC, abstractmethod
from typing import Tuple


class IVariable(ABC):
    @abstractmethod
    def __init__(self, shape: Tuple = (), name: str = "", integer: bool = False):
        self.shape = shape
        self.name = name
        self.integer = integer


class IFunction(ABC):

    @abstractmethod
    def __init__(self, x: IVariable):
        self.x = x

    @abstractmethod
    def evaluate_at(self, x0):
        pass

    @abstractmethod
    def gradient_at(self, x0):
        pass

    @abstractmethod
    def hessian_at(self, x0):
        pass


class IConstraint(ABC):

    @abstractmethod
    def add_constr(self, const_func: IFunction):
        pass


class IObjective(ABC):
    @abstractmethod
    def __init__(self, func: IFunction, sense: str = "minimize"):
        self.func = func
        self.sense = sense

    @abstractmethod
    def get_obj(self, x0):
        pass

    @abstractmethod
    def get_grad(self, x0):
        pass

    @abstractmethod
    def get_hessian(self, x0):
        pass


class IModel(ABC):
    @abstractmethod
    def __init__(self, objective: IObjective, constraints: IConstraint):
        self.objective = objective
        self.constraints = constraints
        self.results = {}
