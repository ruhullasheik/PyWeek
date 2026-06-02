# Tool Practice

Exercises that practice Git, uv, and Ruff in realistic workflows.

## Git: Merge Conflict Resolution

1. Create two branches from main: `feature-a` and `feature-b`
2. In both branches, edit the same lines of `conflict.txt`
3. Commit both
4. Merge `feature-a` into `main`
5. Try to merge `feature-b` — resolve the conflict
6. Commit the resolution

## Git: Interactive Rebase

1. Make 5 small commits on a branch
2. Squash the last 3 into one commit
3. Reword the first commit message
4. Verify the result with `git log`

## uv: Project Setup

1. Create a new project: `uv init my-project`
2. Add a dependency: `uv add requests`
3. Add a dev dependency: `uv add --dev pytest`
4. Run `uv sync` and verify `pyproject.toml`

## Ruff: Code Quality

1. Take a day-02 exercise file
2. Add deliberate style issues (bad spacing, naming, long lines)
3. Run `ruff check` — read every warning
4. Run `ruff check --fix` — see what auto-fixes
5. Run `ruff format` — see the reformatted output
6. Compare before and after

## GitHub: Fork Workflow (simulated)

1. Create a local bare repo as "upstream"
2. Clone it as your "fork"
3. Make a change, push to fork
4. Practice: fetch upstream, rebase, force-push
