"""Make the synthetic moons data and a stratified train/test split."""

import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split


def make_data(n_samples, noise, scale_factor, seed):
    """Return features X and labels y.

    Feature 1 is multiplied by scale_factor so distances are dominated by
    that axis unless you scale inside a Pipeline later.
    """
    # TODO: generate two-moons data with make_moons(...).
    #   - pass n_samples, noise, and random_state=seed
    #   - convert X and y to numpy arrays (float / int)
    #   - multiply column 1 of X by scale_factor
    #   - return X, y
    raise NotImplementedError("TODO: implement make_data")


def split_data(X, y, test_size, seed):
    """Stratified train/test split. Same seed -> same split."""
    # TODO: call train_test_split with:
    #   - test_size=test_size
    #   - random_state=seed
    #   - stratify=y
    #   Return X_train, X_test, y_train, y_test
    raise NotImplementedError("TODO: implement split_data")
