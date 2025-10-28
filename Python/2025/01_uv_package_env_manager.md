# UV - Quick Reference

A concise guide to using [`uv`](https://docs.astral.sh/uv/) for Python project management:
installation, project setup, dependency management, Python version handling, and more.

---

## TL;DR

```bash
# Install 'uv' on macOS, Linux, or WSL (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install 'uv' on Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Install 'uv' on Windows with ThreatLocker (custom install paths)
powershell -ExecutionPolicy ByPass -c {
  $env:UV_INSTALL_DIR =        "C:\Endava\EndevLocal\.local\uv\bin";
  $env:UV_PYTHON_INSTALL_DIR = "C:\Endava\EndevLocal\.local\uv\python";
  $env:UV_PYTHON_BIN_DIR =     "C:\Endava\EndevLocal\.local\uv\bin\python";
  $env:UV_CACHE_DIR =          "C:\Endava\EndevLocal\.local\uv\cache";
  irm https://astral.sh/uv/install.ps1 | iex
}
# Add to PATH
$env:Path = "C:\Endava\EndevLocal\.local\uv\bin;$env:Path"

# Restart your shell

# For a git-cloned project
uv sync
uv run <file.py>

# To create a new project
uv init <project_dir>
cd <project_dir>
uv run .\hello.py
uv add <python_package_name_1> <python_package_name_2> ...
uv run <file.py>
```

---

## Step-by-Step Guide

### 1. Installing `uv`

```bash
# macOS & Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Windows with ThreatLocker (custom install paths)
$env:UV_PYTHON_INSTALL_DIR = "C:\Endava\EndevLocal\.local\uv\python"
powershell -ExecutionPolicy ByPass -c {
  $env:UV_INSTALL_DIR = "C:\Endava\EndevLocal\.local\uv\bin";
  irm https://astral.sh/uv/install.ps1 | iex
}

# Using pip
pip install uv

# Update uv
uv self update
```

---

### 2. Creating a New Python Project

```bash
# Option 1
mkdir <project_dir>
cd <project_dir>
uv init

# Option 2
uv init <project_dir>
cd <project_dir>

# Specify Python version
uv init <project_dir> --python 3.12
cd <project_dir>
```

---

### 3. Creating and Testing the Python Environment

```bash
# Environment is created automatically when running a Python file.
uv run .\hello.py
```
- No need to activate/deactivate environments.
- Uses `pyproject.toml` and `uv.lock` for reproducibility.

---

### 4. Working with Dependencies

```bash
# Sync dependencies (e.g., after git clone or pull)
uv sync

# Add a new dependency (latest version)
uv add <python_package_name>

# Add/upgrade/downgrade to a specific version
uv add <python_package_name>=='0.115'

# Export lockfile to requirements.txt (for pip or other legacy tools)
uv export --format requirements-txt > requirements.txt

# Add dependencies from requirements.txt (for compatibility with pip or other tools)
uv add -r requirements.txt

# Remove a dependency
uv remove <python_package_name>

# View dependency tree
uv tree

# Update a dependency to latest compatible version
uv remove <python_package_name>
uv add <python_package_name>
```

---

### 5. Installing and Managing Python Versions

```bash
# Set custom Python binary install directory (Windows)
# This is necessary if you have ThreatLocker or similar security software
# that restricts access to certain directories.
# Default value is $env:APPDATA, where APPDATA=C:\Users\<windows_user>\AppData\Roaming
$env:UV_PYTHON_INSTALL_DIR = "C:\Endava\EndevLocal\.local\uv\python"

# Install specific Python versions
uv python install 3.11 3.12 pypy@3.10

# List available Python versions
uv python list

# Run with a specific Python version
uv run --python 3.12 -- python
uv run --python 3.13 <file.py>
uv run --python pypy@3.10 <file.py>

# Run a Python module
uv run python -m <module_name> <args>
```

---

### 6. Other Useful Commands & Options

```bash
# uv uses the pyproject.toml file to specify the main dependencies of the project,
# and the uv.lock file to specify all dependencies with hashes to create a
# reproducible environment always.

# The pyproject.toml file can be modified to remove dependency restrictions
# and attempt to update the package to the latest compatible version.

# Upgrade a package in the lockfile
uv lock --upgrade-package <python_package_name>

# Create a lockfile
uv lock

# Build distribution archives
uv build

# Publish to a package index
uv publish

# Connect local repo to GitHub
git remote add origin git@github.com:<user>/<repo>.git
git push -u origin main

# Check/set environment variables (Powershell)
dir env:
$env:UV_PYTHON_INSTALL_DIR
$env:UV_PYTHON_INSTALL_DIR = "C:\Endava\EndevLocal\.local\uv\python"

# Add to PATH
set Path=C:\Endava\EndevLocal\.local\uv\bin;%Path%   # cmd
$env:Path = "C:\Endava\EndevLocal\.local\uv\bin;$env:Path"   # powershell

# Show Python/tools binary directories
uv python dir
uv tool dir

# Uninstall uv and clean up
uv cache clean
rm -r "$(uv python dir)"
rm -r "$(uv tool dir)"
rm $HOME\.local\bin\uv.exe
rm $HOME\.local\bin\uvx.exe

# Other environment variables
$env:UV_INSTALL_DIR =        "C:\Endava\EndevLocal\.local\uv\bin"
$env:UV_PYTHON_BIN_DIR =     "C:\Endava\EndevLocal\.local\uv\bin\python"
$env:UV_PYTHON_INSTALL_DIR = "C:\Endava\EndevLocal\.local\uv\python"
$env:UV_CACHE_DIR =          "C:\Endava\EndevLocal\.local\uv\cache"
```

---

## CI/CD & Containerization Examples

### `.gitlab-ci.yml` with UV

```yaml
variables:
  UV_VERSION: 0.5
  PYTHON_VERSION: 3.12
  BASE_LAYER: ubuntu:24.04
stages:
  - analysis
uv:
  stage: analysis
  image: ghcr.io/astral-sh/uv:$UV_VERSION-python$PYTHON_VERSION-$BASE_LAYER
  script:
  - uv sync --frozen
uv-install:
  variables:
  UV_CACHE_DIR: .uv-cache
  cache:
  key:
    files:
    - uv.lock
  paths:
    - $UV_CACHE_DIR
  script:
  - uv sync --frozen
  - uv cache prune --ci
```

---

### `Dockerfile`

```dockerfile
FROM ghcr.io/astral-sh/uv:debian
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen --no-install-project
COPY . .
RUN uv sync --frozen
CMD ["python", "main.py"]
```

---

### `docker-compose.yml`

```yaml
services:
  app:
  build:
    context: .
    dockerfile: Dockerfile
  volumes:
    - .:/app
  environment:
    - UV_COMPILE_BYTECODE=1
  command: ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
```

---

### FastAPI Optimized Dockerfile

```dockerfile
FROM python:3.12-slim AS builder
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project
COPY . .
RUN uv sync --frozen

FROM python:3.12-slim
COPY --from=builder /app /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
```

---

## Additional Tips

- `uv init --app` — Initialize an application project.
- `uv add fastapi --extra standard`
- `uv add ruff --dev`
- `uv add pyright --dev`
- `ENV UV_COMPILE_BYTECODE=1` — Enable Python bytecode compilation for faster startup.

---

## References

- [UV Documentation: Getting Started](https://docs.astral.sh/uv/getting-started/installation/)
- [UV CLI Reference](https://docs.astral.sh/uv/reference/cli/)
- [UV on PyPI](https://pypi.org/project/uv/)
- [UV GitHub Repository](https://github.com/astral-sh/uv)

### License
This document is licensed under the [MIT License](https://opensource.org/licenses/MIT).

### Author
Leonardo Calderon - [GitHub Profile](https://github.com/en-lcalderon/)


> **Note:** This guide is a compilation of information from official UV documentation and community resources. The author of this document is not affiliated with the UV project and does not claim original authorship of the content. For the most accurate and up-to-date details, always refer to the [official UV documentation](https://docs.astral.sh/uv/).
