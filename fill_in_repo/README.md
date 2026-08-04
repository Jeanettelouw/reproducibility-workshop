# Reproducible KNN (fill-in)

Skeleton project for the workshop. Folder layout and function **signatures**
match the solution; the bodies marked `# TODO` are yours to complete.

## When to use this

1. Audit the messy notebook in `starter_repo/` first.
2. Come here to refactor into functions + config + a run script.
3. Only open `solution_repo/` if you are stuck or after you finish a checkpoint.

## Setup

Same commands on macOS, Linux, and Windows (Anaconda Prompt, or a terminal
where `conda` is initialised).

If you already created the workshop env for `starter_repo/`, reuse it:

```bash
conda activate reproducible-knn
cd fill_in_repo
pip install -e .
# or: pip install -r requirements.txt && pip install -e .
```

First time (create the env from scratch):

```bash
conda create -n reproducible-knn python=3.12 -y
conda activate reproducible-knn
cd fill_in_repo
pip install -e .
```

For the exploration notebook, install Jupyter in the same env (once), then
select the **reproducible-knn** kernel:

```bash
pip install jupyterlab ipykernel
jupyter lab
```

## What you fill in

| File | Your job |
|------|----------|
| `reproducible_knn/data.py` | `make_data`, `split_data` |
| `reproducible_knn/model.py` | `make_knn`, `choose_k` |
| `reproducible_knn/run.py` | body of `run_experiment`; config load + seed override in `main()` |
| `config.yaml` | confirm / set the experiment settings |

Already provided (do not rewrite unless you want to): package `__init__.py`,
`load_config`, figure-saving helper, argparse setup / print summary in
`main()`, `pyproject.toml`, `requirements.txt`.

## Check your work

After the TODOs compile (with `reproducible-knn` activated):

```bash
python -m reproducible_knn.run
python -m reproducible_knn.run --seed 1
```

Same seed twice → identical `outputs/run/metrics.json`.
Different seed → metrics change.

You can also explore via `notebooks/01_clean_knn_exploration.ipynb` once the
functions exist — use the **reproducible-knn** kernel.
