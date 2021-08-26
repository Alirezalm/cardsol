from numpy.random import randn
from numpy import allclose
from cardsol.problem import QuadraticForm, AffineForm
from cardsol.problem import Variable

n = 5

x = Variable(shape = (n, 1), name = "x")
Q = randn(n, n)
q = randn(n, 1)
d = randn(1)
x0 = randn(n, 1)

f_q = QuadraticForm(Q, q, x)
f_a = AffineForm(q, d, x)


def test_quad_eval():
    assert 0.5 * x0.T @ Q @ x0 + q.T @ x0 == f_q.evaluate_at(x0)


def test_guad_grad():
    assert allclose(Q @ x0 + q, f_q.gradient_at(x0))


def test_quad_hess():
    assert allclose(Q, f_q.hessian_at(x0))


def test_affine_eval():
    assert q.T @ x0 + d == f_a.evaluate_at(x0)


def test_affine_grad():
    assert allclose(q, f_a.gradient_at(x0))


def test_affine_hess():
    assert allclose(0, f_a.hessian_at(x0))
