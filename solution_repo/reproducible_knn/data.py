"""Make the synthetic moons data and a stratified train/test split."""

import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split


def make_data(n_samples, noise, scale_factor, seed):
    """Return features X and labels y.
    Feature 1 is multiplied by scale_factor so distances are dominated by
    that axis unless you scale inside a Pipeline later.
    """
    X, y = make_moons(n_samples=n_samples, noise=noise, random_state=seed)
    X = np.asarray(X, dtype=float).copy()
    y = np.asarray(y, dtype=int).copy()
    X[:, 1] *= scale_factor
    return X, y


def split_data(X, y, test_size, seed):
    """Stratified train/test split. Same seed -> same split."""
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=seed,
        stratify=y,
    )
