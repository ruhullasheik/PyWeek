# PyWeek Git Workflow

## How to Use This Repo

Each day is a separate Git branch. You switch once per day, work through the content, and switch again tomorrow.

### Daily Flow

```bash
# Start your day
git switch main
git pull
git switch day-00-tools   # or day-01-variables, etc.

# Work through the content
# ... code, exercises, experiments ...

# Optional: save your work on a personal fork
git add .
git commit -m "my day-00 work"
git push origin day-00-tools
```

### Branch Map

```
main ────────────── graduation hub (capstones, interview prep)
  │
  ├── day-00-tools      ─── Environment & Git
  ├── day-01-variables  ─── Types, I/O
  ├── day-02-control    ─── Loops, conditionals
  ├── day-03-functions  ─── Functions, Ruff
  ├── day-04-data       ─── Collections
  ├── day-05-modules    ─── Imports, packages
  ├── day-06-oop        ─── Classes & beyond
  └── day-07-project    ─── Capstone project
```

**Don't skip days.** Each one builds on the last.
