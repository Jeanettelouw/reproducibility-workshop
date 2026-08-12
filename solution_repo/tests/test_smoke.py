"""Minimal smoke checks for instructors / CI. Students do not need to write these."""

import json
from pathlib import Path

from reproducible_knn.data import make_data, split_data
from reproducible_knn.model import choose_k, make_knn
from reproducible_knn.run import run_experiment


def test_same_seed_same_data():
    a = make_data(100, 0.2, 10.0, seed=7)
    b = make_data(100, 0.2, 10.0, seed=7)
    assert (a[0] == b[0]).all() and (a[1] == b[1]).all()


def test_split_sizes():
    X, y = make_data(100, 0.2, 10.0, seed=1)
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.3, seed=1)
    assert len(X_train) + len(X_test) == 100
    assert len(y_train) == len(X_train)


def test_pipeline_has_scaler_when_requested():
    pipe = make_knn(k=3, use_scaling=True)
    assert "scaler" in pipe.named_steps
    pipe2 = make_knn(k=3, use_scaling=False)
    assert "scaler" not in pipe2.named_steps


def test_choose_k_returns_value_from_grid():
    X, y = make_data(120, 0.2, 10.0, seed=2)
    X_train, _, y_train, _ = split_data(X, y, test_size=0.3, seed=2)
    k_values = [3, 5, 7]
    best_k, results = choose_k(
        X_train, y_train, k_values, use_scaling=True, seed=2, cv_folds=3
    )
    assert best_k in k_values
    assert len(results) == len(k_values)


def test_run_writes_metrics(tmp_path):
    cfg = {
        "seed": 3,
        "n_samples": 80,
        "noise": 0.2,
        "scale_factor": 10.0,
        "test_size": 0.3,
        "k_values": [3, 5],
        "use_scaling": True,
        "cv_folds": 3,
        "output_dir": str(tmp_path / "run"),
    }
    out_dir, metrics = run_experiment(cfg)
    assert (out_dir / "metrics.json").exists()
    assert (out_dir / "cv_results.csv").exists()
    assert (out_dir / "config_used.yaml").exists()
    loaded = json.loads(Path(out_dir / "metrics.json").read_text())
    assert loaded["best_k"] == metrics["best_k"]
