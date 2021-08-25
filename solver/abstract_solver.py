from numpy import ndarray
from abc import ABC, abstractmethod

from problem.model import IModel



class IPrimalSolver(ABC):

    @abstractmethod
    def solve(self, model: IModel, fixed_binary: ndarray):
        pass


class IMasterSolver(ABC):
    @abstractmethod
    def solve(self, model: IModel, fixed_continuous: ndarray):
        pass
