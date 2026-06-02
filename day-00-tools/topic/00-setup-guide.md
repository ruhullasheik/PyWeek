# Setup Guide

Choose your OS and follow the steps.

## Windows

### 1. Install Python
- Download from [python.org](https://python.org) (3.10+)
- **Check** "Add Python to PATH" during installation
- Verify: `python --version`

### 2. Install uv (Fast Python package manager)
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```
- Verify: `uv --version`

### 3. Install Git
```powershell
winget install --id Git.Git -e --source winget
```
- Verify: `git --version`

### 4. Terminal
- Use **PowerShell 7+** (not the old Windows PowerShell)
- Install from: https://github.com/PowerShell/PowerShell

---

## macOS

### 1. Install Homebrew (if not installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Python
```bash
brew install python@3.12
```
- Verify: `python3 --version`

### 3. Install uv
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
- Verify: `uv --version`

### 4. Install Git
```bash
brew install git
```
- Verify: `git --version`

---

## Linux (Ubuntu/Debian)

### 1. Install Python
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```
- Verify: `python3 --version`

### 2. Install uv
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
- Restart your shell, then: `uv --version`

### 3. Install Git
```bash
sudo apt install git
```
- Verify: `git --version`

---

## Verify Everything

Run this from your terminal:

```bash
# Windows (PowerShell)
python --version && uv --version && git --version

# macOS / Linux
python3 --version && uv --version && git --version
```

You should see three version numbers — no errors.
