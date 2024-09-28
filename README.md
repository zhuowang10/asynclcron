# asynclcron
lightweight cron schedule on asyncio, requires python 3.7+. [croniter](https://pypi.org/project/croniter/) is used.

# install

```bash
pip install asynclcron
```

# example
it's very simple to use, please refer to [source code of test schedule](tests/run_lcron.py)

to run test schedule
```bash
# in project root
python3 -m tests.run_lcron
```

# development
## setup dev env
```bash
# in vscode terminal:
python3 -m venv venv
```

```bash
## reopen vscode terminal, venv should show
pip install croniter
```

## unit test
```bash
## run test
python3 -m unittest
```

## packaging and publish
```
rm -rf dist
python3 -m build
python3 -m twine upload dist/*
```
