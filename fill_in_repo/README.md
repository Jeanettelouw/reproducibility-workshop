# Reproducible KNN (fill-in)

Skeleton project for the workshop. Folder layout and function **signatures**
match the solution; the bodies marked `# TODO` are yours to complete.

## When to use this

1. Audit the messy notebook in `starter_repo/` first.
2. Come here to refactor into functions + config + a run script.
3. Only open `solution_repo/` if you are stuck or after you finish a checkpoint.

## Setup

**macOS / Linux**

```bash
cd fill_in_repo
python -m venv .venv
source .venv/bin/activate
pip install -e .
# or: pip install -r requirements.txt && pip install -e .
```

**Windows (Command Prompt)**

```bat
cd fill_in_repo
python -m venv .venv
.venv\Scripts\activate.bat
pip install -e .
REM or: pip install -r requirements.txt && pip install -e .
```

**Windows (PowerShell)**

```powershell
cd fill_in_repo
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
# or: pip install -r requirements.txt; pip install -e .
```

If PowerShell blocks the activate script, run once (current user only):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Optional with `uv` (same on all platforms):

```bash
uv sync
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

After the TODOs compile (same commands on all platforms):

```bash
python -m reproducible_knn.run
python -m reproducible_knn.run --seed 1
```

Same seed twice → identical `outputs/run/metrics.json`.
Different seed → metrics change.

You can also explore via `notebooks/01_clean_knn_exploration.ipynb` once the
functions exist.
