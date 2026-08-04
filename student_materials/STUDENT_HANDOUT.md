# Student handout

**Workshop:** From a messy KNN notebook to a reproducible computational project

## Your objective

Transform a notebook that “works on my machine” into a small project another
person can clone, configure, and run from the command line — obtaining the same
numerical results.

**Research question you will preserve:**

> How do feature scaling and the number of neighbours, *k*, affect KNN
> classification performance and its decision boundary?

## Before you start

1. Install Git (and optionally [`uv`](https://docs.astral.sh/uv/)).
2. Obtain the workshop folders from your instructor (`starter_repo/`,
   `fill_in_repo/`).
3. Optional: skim the solution repo only when invited; the learning is in the
   fill-in path.

### Step A — Audit the messy notebook

**macOS / Linux**

```bash
cd starter_repo
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

**Windows (Command Prompt)**

```bat
cd starter_repo
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
jupyter lab
```

**Windows (PowerShell)**

```powershell
cd starter_repo
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```

If PowerShell blocks activation, run once:
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Open `notebooks/00_messy_knn_experiment.ipynb` and run all cells once.

### Step B — Complete the fill-in project

After the audit, switch to the skeleton:

**macOS / Linux**

```bash
cd ../fill_in_repo
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

**Windows (Command Prompt)**

```bat
cd ..\fill_in_repo
python -m venv .venv
.venv\Scripts\activate.bat
pip install -e .
```

**Windows (PowerShell)**

```powershell
cd ..\fill_in_repo
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

Fill in every `# TODO` in `reproducible_knn/`. The folder layout and function
names already match a working solution — you supply the missing bodies.

---

## Part 0 — The audit

Without “fixing” the notebook yet, list every reproducibility risk you notice.
For each, note what you observed and how it could change a scientific conclusion.

Checkpoint questions:

- Do you get the same accuracy if you restart the kernel and rerun?
- Where does randomness enter?
- Was the test set used only for final evaluation?

---

## Part 1 — Extract functions (`fill_in_repo`)

In `reproducible_knn/data.py` and `model.py`, complete:

- `make_data(...)` — generate the synthetic moons data (with a scale factor)
- `split_data(...)` — stratified train/test split
- `make_knn(...)` — build a KNN model, optionally with `StandardScaler` in a
  `Pipeline`

Success looks like: the exploration notebook *calls* these functions instead of
pasting the same fitting code three times.

**What is a package?** A folder of related functions (with an empty
`__init__.py`) so you can write `from reproducible_knn.data import make_data`.
You do not need fancy software design — just a folder.

---

## Part 2 — Make randomness an explicit input

- Choose a master seed and pass it into `make_moons` / `train_test_split` /
  the CV splitter (the TODOs already ask for a `seed` argument).
- Record the seed next to any saved results (see `config.yaml` and metrics).
- Confirm: same seed → same split and same selected *k*; new seed → change.

---

## Part 3 — Stop leaking information

In `make_knn` / `choose_k`, make sure that:

1. You **do not** standardise the full dataset before splitting.
2. Scaling, if used, lives inside a `sklearn.pipeline.Pipeline`.
3. You choose *k* with **cross-validation on the training set**.
4. You evaluate the held-out test set **exactly once** after selection
   (that last step belongs in `run_experiment`).

Checkpoint: can you point to the line where the test set is first touched for
scoring?

---

## Part 4 — One config file + a run script

`config.yaml` is already sketched. Complete `run_experiment` in
`reproducible_knn/run.py` so it:

1. loads the YAML (helper provided)
2. calls your functions
3. saves `metrics.json` (and figures) under `outputs/run/`

Run it without Jupyter:

```bash
python -m reproducible_knn.run
python -m reproducible_knn.run --seed 42
```

(`-m` means “run this file as a program.” That *is* the CLI for this workshop.)

---

## Part 5 — Lock the environment

Pick one:

- `pyproject.toml` + `uv.lock` + `uv sync --locked`, or
- a pinned `requirements.txt` + `pip install -r requirements.txt`

Either way, someone else should be able to recreate your library versions.

---

## Part 6 — Verify by running twice

You do **not** need a large test suite. Do this:

**macOS / Linux**

```bash
python -m reproducible_knn.run --seed 1
cp outputs/run/metrics.json /tmp/a.json
python -m reproducible_knn.run --seed 1
# compare /tmp/a.json with outputs/run/metrics.json — they should match
```

**Windows (Command Prompt)**

```bat
python -m reproducible_knn.run --seed 1
copy outputs\run\metrics.json %TEMP%\a.json
python -m reproducible_knn.run --seed 1
REM compare %TEMP%\a.json with outputs\run\metrics.json — they should match
```

**Windows (PowerShell)**

```powershell
python -m reproducible_knn.run --seed 1
Copy-Item outputs\run\metrics.json $env:TEMP\a.json
python -m reproducible_knn.run --seed 1
# compare $env:TEMP\a.json with outputs\run\metrics.json — they should match
```

Then change the seed and confirm the metrics change.

---

## Final challenge — the clean machine

On a fresh clone (or a classmate’s laptop):

```bash
uv sync --locked          # or: pip install -e . / pip install -r requirements.txt
python -m reproducible_knn.run
```

If a stranger can do only this and match your numbers (same seed), you succeeded.

## Closing reflection

Write three sentences:

1. What made the original notebook persuasive but unreliable?
2. Which fix most improved **statistical** trustworthiness (not just neatness)?
3. What would you still not trust without further evidence?
