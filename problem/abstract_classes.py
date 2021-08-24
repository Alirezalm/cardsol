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


class IConstraint(ABC):

    @abstractmethod
    def add_constr(self, const_func: IFunction):
        pass


class IObjective(ABC):
    @abstractmethod
    def get_obj(self, x0):
        pass

    @abstractmethod
    def get_grad(self, x0):
        pass

    @abstractmethod
    def get_hessian(self, x0):
        pass
