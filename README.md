# Reproducibility workshop

Materials for a hands-on session that turns a messy Jupyter notebook into a
**small** reproducible project. The scientific thread is a K-nearest neighbours
classification experiment on synthetic two-moons data with unequal feature
scales.

Aimed at students with bare-minimum Python scripting skills.

## Layout

| Path | Role |
|---|---|
| `starter_repo/` | Intentionally flawed KNN notebook students audit first |
| `fill_in_repo/` | Skeleton solution: signatures + TODOs students complete |
| `solution_repo/` | (NOT ADDED YET) Fully filled reference; reveal progressively |
| `student_materials/` | Student handout |

**Suggested path:** audit in `starter_repo/` → complete TODOs in `fill_in_repo/`
→ consult `solution_repo/` only when invited (or after a checkpoint).

## Central message

> A result is not reproducible merely because the code exists. Another person
> must be able to recreate the environment, rerun the complete workflow, obtain
> the same outputs, and verify how those outputs were produced.

## Solution in one glance

Same commands on macOS, Linux, and Windows:

```bash
conda create -n reproducible-knn python=3.12 -y
conda activate reproducible-knn
cd solution_repo
pip install -e .
python -m reproducible_knn.run
```

That is the whole CLI: one config file, three short modules, saved metrics under
`outputs/run/`.

## Quick links

- Student exercises: `student_materials/STUDENT_HANDOUT.md`
- Fill-in setup: `fill_in_repo/README.md`
- Solution setup: `solution_repo/README.md`
