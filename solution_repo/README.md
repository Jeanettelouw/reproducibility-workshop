# Reproducible KNN (solution)

A **small** example of turning a messy notebook into something another person can
rerun. Aimed at students with basic Python scripting — not a software-engineering
showcase.

## Three commands

Same on macOS, Linux, and Windows (once the environment is active):

```bash
uv sync --locked                 # or: pip install -e .
python -m reproducible_knn.run   # run the experiment (no Jupyter)
python -m reproducible_knn.run --seed 42
```

### Activate a venv (if not using `uv run`)

**macOS / Linux**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

**Windows (Command Prompt)**

```bat
python -m venv .venv
.venv\Scripts\activate.bat
pip install -e .
```

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

`-m` means “run this file as a program.” That is the whole CLI.

## What each file is for

| Path | Role |
|------|------|
| `config.yaml` | All settings (seed, sample size, *k* grid, scaling flag) |
| `reproducible_knn/data.py` | `make_data`, `split_data` |
| `reproducible_knn/model.py` | `make_knn`, `choose_k` (CV on train only) |
| `reproducible_knn/run.py` | Load config → run → save `outputs/run/` |
| `reproducible_knn/__init__.py` | Empty; makes the folder importable |
| `notebooks/01_clean_knn_exploration.ipynb` | Calls the same functions for exploration |
| `pyproject.toml` / `uv.lock` | Pin the environment |
| `requirements.txt` | Pip fallback |

## What a run writes

Under `outputs/run/`:

- `config_used.yaml` — settings that produced the result
- `metrics.json` — best *k*, CV accuracy, test accuracy
- `cv_results.csv` — CV table for each *k*
- `figures/dataset.png`, `figures/decision_boundary.png`

## Verify reproducibility

**macOS / Linux**

```bash
python -m reproducible_knn.run --seed 1
cp outputs/run/metrics.json /tmp/a.json
python -m reproducible_knn.run --seed 1
# /tmp/a.json and outputs/run/metrics.json should match
```

**Windows (Command Prompt)**

```bat
python -m reproducible_knn.run --seed 1
copy outputs\run\metrics.json %TEMP%\a.json
python -m reproducible_knn.run --seed 1
REM %TEMP%\a.json and outputs\run\metrics.json should match
```

**Windows (PowerShell)**

```powershell
python -m reproducible_knn.run --seed 1
Copy-Item outputs\run\metrics.json $env:TEMP\a.json
python -m reproducible_knn.run --seed 1
# $env:TEMP\a.json and outputs\run\metrics.json should match
```

## Design rules baked in

1. One master **seed** drives data, split, and CV shuffling.
2. Scaling (if any) is inside a **Pipeline**, not fit on the full dataset before the split.
3. Choose *k* with CV on the **training** set; score the **test** set once.
4. Settings live in **config**, not buried in cells.

## Instructor note

Students normally complete the twin layout in `fill_in_repo/` (same files, `# TODO`
stubs). This folder is the filled reference.

`tests/test_smoke.py` is optional CI glue. Students are not expected to write a
test suite — running the CLI twice is enough for the workshop.
