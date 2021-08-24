from numpy.random import randn
from numpy import allclose
from problem.functions import QuadraticForm
from problem.variables import Variable

n = 5

x = Variable(shape = (n, 1), name = "x")
Q = randn(n, n)
q = randn(n, 1)

x0 = randn(n, 1)

f = QuadraticForm(Q, q, x)


def test_quad_eval():
    assert 0.5 * x0.T @ Q @ x0 + q.T @ x0 == f.evaluate_at(x0)


def test_guad_grad():
    assert allclose(Q @ x0 + q, f.gradient_at(x0))


def test_quad_hess():
    assert allclose(Q, f.hessian_at(x0))
