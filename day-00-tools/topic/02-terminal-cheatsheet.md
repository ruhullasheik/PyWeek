# Terminal Cheatsheet

You'll live in the terminal this week. Master these commands.

## Navigation

| Command | Windows (PowerShell) | macOS / Linux |
|---|---|---|
| List files | `ls` | `ls` |
| Change directory | `cd folder` | `cd folder` |
| Go up | `cd ..` | `cd ..` |
| Home | `cd ~` | `cd ~` |
| Current path | `pwd` | `pwd` |
| Create directory | `mkdir name` | `mkdir name` |
| Create file | `New-Item file.py` | `touch file.py` |
| Delete file | `Remove-Item file.py` | `rm file.py` |
| Read file | `Get-Content file.py` | `cat file.py` |
| Clear screen | `cls` | `clear` |

## Running Python

```bash
# Run a script
python script.py          # Windows
python3 script.py         # macOS / Linux

# Interactive mode
python                    # REPL — type code directly
exit()                    # Quit REPL
```

## Git Basics

```bash
git init          # Start tracking a folder
git status        # What changed?
git add file.py   # Stage a file
git commit -m "msg"  # Save a snapshot
git log           # See history
```

## uv Basics

```bash
uv --version                      # Check version
uv venv                           # Create virtual env
uv pip install requests           # Install a package
uv pip list                       # List installed packages
```
