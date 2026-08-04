# Reproducibility checklist (simple version)

- [ ] Modelling logic lives in `reproducible_knn/` functions, not only in a notebook
- [ ] One flat `config.yaml` holds seed, sample size, k grid, scaling flag
- [ ] Master seed drives data generation, split, and CV shuffling
- [ ] Scaling (if used) is inside a `Pipeline`, never fit on the full dataset before the split
- [ ] Choose `k` with CV on the **training** set; score the test set **once**
- [ ] `python -m reproducible_knn.run` writes `outputs/run/` (config copy, metrics, figures)
- [ ] `pyproject.toml` + lockfile (or `requirements.txt`) pin the environment
- [ ] Same seed twice → same `metrics.json`; different seed → different results
