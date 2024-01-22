import cvxpy as cp
import numpy as np
import sys

# Problem data
n = int(sys.argv[1])
num_workers = 32
throughputs = np.random.uniform(0, 1, (n, 3))
priority_weights = np.random.uniform(0, 1, (n, 1))
scale_factors_array = np.random.uniform(0, 1, (n, 3))

# throughputs = np.ones((n, 3))
# priority_weights = np.ones((n, 1))
# scale_factors_array = np.ones((n, 3))

# constraints
def get_base_constraints(x, scale_factors_array):
    """Return base constraints."""
    return [
        x >= 0,
        cp.sum(cp.multiply(
            scale_factors_array, x), axis=0) <= num_workers,
        cp.sum(x, axis=1) <= 1,
    ]

# Construct the problem
x = cp.Variable(throughputs.shape)
objective = cp.Maximize(
    cp.min(cp.sum(cp.multiply(
        np.multiply(throughputs * priority_weights,
                    scale_factors_array), x), axis=1)))
constraints = get_base_constraints(x, scale_factors_array)
cvxprob = cp.Problem(objective, constraints)

# The optimal objective value is returned by `prob.solve()`.
result = cvxprob.solve(solver='ECOS')

if cvxprob.status != "optimal":
    print('WARNING: Allocation returned by policy not optimal!')


print(cvxprob.solver_stats.solve_time, cvxprob.solver_stats.setup_time)