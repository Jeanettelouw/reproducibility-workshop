# Student handout

**Workshop:** From a messy KNN notebook to a reproducible computational project

## Your objective

Transform a notebook that “works on my machine” into a project another person
can clone, configure, run from the command line, and verify — obtaining the
same numerical results and understanding how they were produced.

**Research question you will preserve:**

> How do feature scaling and the number of neighbours, *k*, affect KNN
> classification performance and its decision boundary?

## Before you start

1. Install [`uv`](https://docs.astral.sh/uv/) and Git.
2. Obtain the `starter_repo/` folder from your instructor.
3. Optional: skim the solution repo only when invited; the learning is in the
   refactor path.

```bash
cd starter_repo
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Open `notebooks/00_messy_knn_experiment.ipynb` and run all cells once.

---

## Part 0 — The audit

Without “fixing” the notebook yet, list every reproducibility or design risk
you notice. For each, note:

- what you observed;
- whether it is mainly **computational**, **software-engineering**, or
  **statistical / experimental-design**;
- how it could change a scientific conclusion.

Checkpoint questions:

- Do you get the same accuracy if you restart the kernel and rerun?
- Where does randomness enter?
- Was the test set used only for final evaluation?

---

## Part 1 — Extract the statistics

Move data generation and model fitting out of ad-hoc cells into functions (or a
small package). Aim for:

- one function to generate the synthetic moons data (with a scale factor);
- one function to create a stratified train/test split;
- one function to build a KNN pipeline (with or without `StandardScaler`).

Success looks like: the notebook *calls* functions instead of pasting the same
fitting code three times.

---

## Part 2 — Make randomness an explicit input

- Choose a master seed and pass it into `make_moons` / `train_test_split` /
  CV splitters.
- Record the seed next to any saved results.
- Confirm: same seed → same split and same selected *k*; new seed → change.

---

## Part 3 — Stop leaking information

Refactor so that:

1. You **do not** standardise the full dataset before splitting.
2. Scaling, if used, lives inside a `sklearn.pipeline.Pipeline`.
3. You choose *k* (and scaling) with **cross-validation on the training set**.
4. You evaluate the held-out test set **exactly once** after selection.

Checkpoint: can you point to the line where the test set is first touched for
scoring?

---

## Part 4 — Configuration + a command-line entry point

Replace hard-coded `n_samples`, `noise`, `k` grids, and paths with YAML (or
similar). Provide a CLI roughly like:

```bash
uv run python -m reproducible_knn.cli \
  dataset=moons \
  preprocessing=scaled \
  experiment=quick
```

Save under a run directory: resolved config, metrics, predictions, metadata,
and figures.

---

## Part 5 — Lock the environment

- Declare dependencies in `pyproject.toml`.
- Produce and commit a lockfile (`uv.lock`).
- Pin Python 3.12 via `.python-version`.

```bash
uv sync --locked
uv run pytest
```

---

## Part 6 — Tests and verification

Add tests for at least:

- same seed → same data;
- train/test indices do not overlap;
- illegal *k* is rejected;
- selected parameters are repeatable;
- CLI smoke run writes artifacts.

Then run:

```bash
uv run python scripts/verify_reproduction.py
```

---

## Final challenge — the clean machine

On a fresh clone (or CI):

```bash
uv sync --locked
uv run pytest
uv run python -m reproducible_knn.cli experiment=quick
uv run python scripts/verify_reproduction.py
```

If a stranger can do only this and match your numbers, you succeeded.

## Closing reflection

Write three sentences:

1. What made the original notebook persuasive but unreliable?
2. Which fix most improved **statistical** trustworthiness (not just neatness)?
3. What would you still not trust without further evidence?
