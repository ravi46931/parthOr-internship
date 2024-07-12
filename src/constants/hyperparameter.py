""" Hyperparameters"""

RIDGE_PARAMS = {
    "alpha": [0.1, 0.5, 1.0, 5.0, 10.0],
    "solver": ["auto", "svd", "cholesky", "lsqr", "sparse_cg", "sag", "saga", "lbfgs"],
}

LASSO_PARAMS = {"alpha": [0.1, 0.5, 1.0, 5.0, 10.0], "selection": ["cyclic", "random"]}

POLYNOMIAL_PARAMS = {"polynomialfeatures__degree": [2, 3, 4]}

"""WRITE THE HYPERPARAMETERS HERE"""

