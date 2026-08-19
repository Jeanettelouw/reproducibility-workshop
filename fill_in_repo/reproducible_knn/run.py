
"""Run the full experiment from the command line (no Jupyter needed).

Usage:
    python -m reproducible_knn.run
    python -m reproducible_knn.run --seed 42
    python -m reproducible_knn.run --config path/to/config.yaml
"""

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import yaml
from sklearn.metrics import accuracy_score, confusion_matrix

from reproducible_knn.data import make_data, split_data
from reproducible_knn.model import choose_k, make_knn


def load_config(path):
    with open(path) as f:
        return yaml.safe_load(f)


def save_figures(X, y, model, out_dir):
    """Save two simple figures: the data and the decision boundary."""
    fig_dir = out_dir / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", edgecolors="k", s=20)
    ax.set_title("Synthetic moons data")
    ax.set_xlabel("feature 0")
    ax.set_ylabel("feature 1 (stretched)")
    fig.tight_layout()
    fig.savefig(fig_dir / "dataset.png", dpi=120)
    plt.close(fig)

    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xs = np.linspace(x_min, x_max, 200)
    ys = np.linspace(y_min, y_max, 200)
    xx, yy = np.meshgrid(xs, ys)
    zz = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    fig, ax = plt.subplots()
    ax.contourf(xx, yy, zz, alpha=0.3, cmap="coolwarm")
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", edgecolors="k", s=20)
    ax.set_title("Final decision boundary")
    fig.tight_layout()
    fig.savefig(fig_dir / "decision_boundary.png", dpi=120)
    plt.close(fig)


def run_experiment(cfg):
    """Full pipeline: data -> split -> choose k on train -> score test once."""
    # TODO: wire the pieces together using values from cfg.
    #
    # 1. X, y = make_data(n_samples=..., noise=..., scale_factor=..., seed=...)
    # 2. X_train, X_test, y_train, y_test = split_data(...)
    # 3. best_k, cv_results = choose_k(X_train, y_train, ...)  # train only!
    # 4. model = make_knn(k=best_k, use_scaling=...)
    #    model.fit(X_train, y_train)
    #    y_pred = model.predict(X_test)
    #    test_accuracy = float(accuracy_score(y_test, y_pred))
    # 5. Create out_dir = Path(cfg["output_dir"]); out_dir.mkdir(...)
    # 6. Write metrics.json with seed, use_scaling, best_k,
    #    best_mean_cv_accuracy, test_accuracy, confusion_matrix
    # 7. Write cv_results.csv and config_used.yaml
    # 8. Call save_figures(X, y, model, out_dir)
    # 9. return out_dir, metrics
    #
    # Config keys you will need: seed, n_samples, noise, scale_factor,
    # test_size, k_values, use_scaling, cv_folds, output_dir

    ##########
    # Given 
    #########
    X, y = make_data(
        n_samples=cfg["n_samples"],
        noise=cfg["noise"],
        scale_factor=cfg["scale_factor"],
        seed=cfg["seed"],
    )

    X_train, X_test, y_train, y_test = split_data(
        X,
        y,
        test_size=cfg["test_size"],
        seed=cfg["seed"],
    )

    best_k, cv_results = choose_k(
        X_train,
        y_train,
        k_values=cfg["k_values"],
        use_scaling=cfg["use_scaling"],
        seed=cfg["seed"],
        cv_folds=cfg["cv_folds"],
    )

    model = make_knn(
        k=best_k,
        use_scaling=cfg["use_scaling"]
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    test_accuracy = float(
        accuracy_score(y_test, y_pred)
    )


    ###### 
    # NEW
    ######
    out_dir = Path(cfg["output_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)

    cm = confusion_matrix(y_test, y_pred).tolist()

    metrics = {
        "seed": cfg["seed"],
        "use_scaling": cfg["use_scaling"],
        "best_k": int(best_k),
        "best_mean_cv_accuracy": float(
            cv_results.iloc[0]["mean_cv_accuracy"]
        ),
        "test_accuracy": test_accuracy,
        "confusion_matrix": cm,
    }

    with open(out_dir / "metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    cv_results.to_csv(
        out_dir / "cv_results.csv",
        index=False
    )

    with open(out_dir / "config_used.yaml", "w") as f:
        yaml.safe_dump(cfg, f)

    save_figures(X, y, model, out_dir)

    return out_dir, metrics


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Run the reproducible KNN experiment."
    )
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to the YAML config file (default: config.yaml)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional override for the seed in the config file",
    )
    args = parser.parse_args(argv)

    # TODO: load config, apply optional CLI seed override, run the experiment.
    #
    # 1. cfg = ??????
    cfg = load_config(args.config)
    
    if args.seed is not None: 
        cfg["seed"] = args.seed
    # 3. out_dir, metrics = ?????
    out_dir, metrics = run_experiment(cfg)

    print(f"Wrote results to {out_dir.resolve()}")
    print(
        f"best_k={metrics['best_k']}  "
        f"cv={metrics['best_mean_cv_accuracy']:.4f}  "
        f"test={metrics['test_accuracy']:.4f}"
    )


if __name__ == "__main__":
    main()
