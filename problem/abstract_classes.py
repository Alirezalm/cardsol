from abc import ABC, abstractmethod


class IVariable(ABC):

    pass


class IFunction(ABC):

    @abstractmethod
    def evaluate_at(self, x0):
        pass

    @abstractmethod
    def gradient_at(self, x0):
        pass

    @abstractmethod
    def hessian_at(self, x0):
        pass
