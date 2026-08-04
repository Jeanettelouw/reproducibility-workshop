# KNN classification experiment

Quick look at how the number of neighbours and feature scaling affect a
K-nearest-neighbours classifier on a two-moons dataset.

The analysis lives in the notebook. Run the cells from top to bottom.

## Running it

```
notebooks/00_messy_knn_experiment.ipynb
```

### Setup

Same commands on macOS, Linux, and Windows (Anaconda Prompt, or a terminal
where `conda` is initialised):

```bash
conda create -n reproducible-knn python=3.12 -y
conda activate reproducible-knn
cd starter_repo
pip install -r requirements.txt
jupyter lab
```

Open `notebooks/00_messy_knn_experiment.ipynb` and select the
**reproducible-knn** kernel (Kernel → Select Kernel / Change Kernel). Then run
the notebook in order.

Figures are written to `outputs/` (create that folder if it is missing).
