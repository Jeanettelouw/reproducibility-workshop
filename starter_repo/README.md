# KNN classification experiment

Quick look at how the number of neighbours and feature scaling affect a
K-nearest-neighbours classifier on a two-moons dataset.

The analysis lives in the notebook. Run the cells from top to bottom.

## Running it

```
notebooks/00_messy_knn_experiment.ipynb
```

### Setup

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

If PowerShell blocks the activate script, run once (current user only):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Open `notebooks/00_messy_knn_experiment.ipynb` and run the notebook in order.
Figures are written to `outputs/` (create that folder if it is missing).
