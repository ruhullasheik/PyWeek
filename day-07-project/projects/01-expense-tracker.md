# CLI Expense Tracker

**Difficulty**: Medium  
**Skills**: JSON, argparse, datetime, CRUD operations

## Spec

Build a CLI tool that tracks personal expenses.

### Features

```
python track.py add --amount 12.50 --category food --description "Lunch"
python track.py add --amount 50 --category transport --description "Monthly pass"
python track.py list                        # Show all expenses
python track.py list --category food        # Filter by category
python track.py list --month 6              # Filter by month
python track.py total                       # Show total spent
python track.py total --category food       # Total by category
python track.py summary                     # Show total per category
python track.py delete --id 1              # Delete by ID
```

### Data Storage

- Store expenses in a JSON file (`~/.pyweek-tracker/data.json`)
- Each expense: `{id, amount, category, description, date}`
- Auto-assign incrementing IDs

### Requirements

- Use `argparse` for CLI
- Use `pathlib` for file paths
- Use `datetime` for dates
- Handle errors gracefully (bad JSON, missing file, invalid ID)
- At least 100 lines of Python

### Extension Ideas

- Export to CSV
- Monthly budget with alerts
- Recurring expenses
