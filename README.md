# Reproducibility workshop

Materials for a hands-on session that turns a messy Jupyter notebook into a
reproducible computational project. The scientific thread is a **K-nearest
neighbours** classification experiment on a synthetic two-moons dataset with
unequal feature scales.

## Layout

| Path | Role |
|---|---|
| `starter_repo/` | Intentionally flawed KNN notebook students audit first |
| `solution_repo/` | Complete, tested, CLI-driven reproducible project |
| `instructor_materials/` | Facilitator guide, handout, answer key, checkpoints, troubleshooting |

Students should begin in `starter_repo/` and only consult `solution_repo/` when
the facilitator invites them to (or after attempting each checkpoint).

## Central message

> A result is not reproducible merely because the code exists. Another person
> must be able to recreate the environment, rerun the complete workflow, obtain
> the same outputs, and verify how those outputs were produced.

## Quick links

- Student exercises: `instructor_materials/STUDENT_HANDOUT.md`
- Facilitator schedule: `instructor_materials/FACILITATOR_GUIDE.md`
- Solution setup: `solution_repo/README.md`
