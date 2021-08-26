from numpy import ndarray
from abc import ABC, abstractmethod

from cardsol.problem.model import IModel


class IPrimalSolver(ABC):

    @abstractmethod
    def solve(self, model: IModel, fixed_binary: ndarray, m_bound):
        pass


class IMasterSolver(ABC):
    @abstractmethod
    def solve(self, cutpool, fixed_continuous: ndarray, k, m):
        pass
