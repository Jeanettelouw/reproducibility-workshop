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
    steps = []
    if use_scaling:
        steps.append(("scaler", StandardScaler()))
    steps.append(("knn", KNeighborsClassifier(n_neighbors=k)))
    return Pipeline(steps)


def choose_k(X_train, y_train, k_values, use_scaling, seed, cv_folds):
    """Pick the best k by stratified CV on the training set.

    Returns (best_k, results_dataframe). The held-out test set is not used.
    """
    cv = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=seed)

    rows = []
    for k in k_values:
        pipe = make_knn(k=k, use_scaling=use_scaling)
        scores = cross_val_score(
            pipe, X_train, y_train, cv=cv, scoring="accuracy"
        )
        rows.append(
            {
                "k": k,
                "mean_cv_accuracy": float(scores.mean()),
                "std_cv_accuracy": float(scores.std()),
            }
        )

    results = pd.DataFrame(rows).sort_values(
        "mean_cv_accuracy", ascending=False
    ).reset_index(drop=True)
    best_k = int(results.loc[0, "k"])
    return best_k, results
