import numpy as np


def pca(X):
    """Return principal components.
    
    Parameters
    ----------
    X : numpy.ndarray
        Point cloud of shape (N, 3), where N is the number of points.
    
    Returns
    -------
    tuple
        Eigenvectors and eigenvalues.
    """
    X = X - X.mean(axis=0)
    C = (X.T @ X) / X.shape[0]
    U, S, _ = np.linalg.svd(C)
    return U, S
