# Todo API Client

**Difficulty**: Medium-Hard  
**Skills**: HTTP, JSON, error handling, CLI

## Spec

Build a CLI client for the JSONPlaceholder API (or any REST API).

API: https://jsonplaceholder.typicode.com/todos

### Features

```
python todo.py list                    # List all todos
python todo.py list --completed true   # Filter completed
python todo.py get 1                   # Get todo by ID
python todo.py create --title "Learn Python" --user-id 1
python todo.py done 1                  # Mark as completed
python todo.py delete 1                # Delete todo
python todo.py stats                   # Show: total, completed, pending
```

### Requirements

- Use `requests` library
- Handle HTTP errors (404, 500) with meaningful messages
- Cache API responses locally to avoid repeated network calls
- Use `argparse` with subparsers for each command
- Format output as a table (use string formatting, not a library)

### Extension Ideas

- Add a `--format json` flag for machine-readable output
- Implement pagination support
- Sync local changes back to the API
