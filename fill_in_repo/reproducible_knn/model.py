"""KNN pipelines and choose k with cross-validation on the training set only."""

import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def make_knn(k, use_scaling):
    """Build a KNN classifier, optionally with StandardScaler as a first step.

    Scaling inside a Pipeline means each CV fold fits the scaler on that fold's
    training rows only — the test set never leaks into scaling.
    """
    # TODO: build and return a sklearn Pipeline.
    #   - if use_scaling is True, first step: ("scaler", StandardScaler())
    #   - always include: ("knn", KNeighborsClassifier(n_neighbors=k))
    # Do NOT fit a scaler on the full dataset outside the Pipeline.
    raise NotImplementedError("TODO: implement make_knn")


def choose_k(X_train, y_train, k_values, use_scaling, seed, cv_folds):
    """Pick the best k by stratified CV on the training set.

    Returns (best_k, results_dataframe). The held-out test set is not used.
    """
    # TODO:
    # 1. Create StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=seed)
    # 2. For each k in k_values:
    #      - build a pipeline with make_knn(k, use_scaling)
    #      - score it with cross_val_score(..., scoring="accuracy")
    #      - record k, mean_cv_accuracy, std_cv_accuracy
    # 3. Put the rows in a DataFrame, sort by mean_cv_accuracy descending
    # 4. Return (best_k, results)  — best_k is the k in the top row
    #
    # Important: only use X_train / y_train here. Never touch the test set.
    raise NotImplementedError("TODO: implement choose_k")
