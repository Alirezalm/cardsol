### Cardinality Constrained Quadratic Optimization Solver (cardsol) 

*cardsol* is a small package for solving mathematical optimization problems of convex Cardinality Constrained Quadratic
Optimization (CCQP) problems. 

cardsol translates the CCQP problem into a Mixed-Integer Optimization Problem (MIQP) provides 
the following algorithms to solve it:

1. Outer Approximation (OA) method
2. LP/NLP based Branch and Bound method
---

### Dependencies
1. Scipy
2. Numpy
3. Gurobipy and gurobi solver

### Example: Random convex CCQP


### Imports

```python
from numpy.random import randn, rand
from numpy import eye
from time import time
from cardsol.problem.constraints import LinearConstraint
from cardsol.problem.functions import QuadraticForm
from cardsol.problem.model import QPModel
from cardsol.problem.objective import QPObjective
from cardsol.problem.variables import Variable
from cardsol.solver.outer_lpnlp.solver import CCQPSolver, LPNLPCCQPSolver
```
#### Define problem Data
```python    
n = ...     # number of variables
k = int(n / 2) # level of cardinality
m = 1
maxiter = 100

Q = rand(n, n) 
Q = Q + Q.T
Q = Q.T @ Q     # Hessian Matrix
c = randn(n, 1) # gradient vector   
```
### Define the model
```python
x = Variable(shape = (n, 1), name = "x")

obj_func = QuadraticForm(Q, c, x)

objective = QPObjective(obj_func, sense = "minimize")

constr = LinearConstraint()

model = QPModel(objective, constr)
```


### Instantiate Solvers
```python
multiple_tree = CCQPSolver(model)

single_tree = LPNLPCCQPSolver(model)
```

### Solve the model

```python
start_single = time()
obj_2 = single_tree.solve(k, m)
end_single = time() - start_single

start_multiple = time()
_, obj_1 = multiple_tree.solve(k, m, 100)
end_multiple = time() - start_multiple
```

### Creating Docker Image

```commandline
sudo docker build .
```