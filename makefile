
# ---- Setup Commands ----
setup:
	python -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt
	source .venv/bin/activate && pre-commit install

setup3:
	python3 -m venv .venv
	source .venv/bin/activate && pip3 install -r requirements.txt
	source .venv/bin/activate && pre-commit install

# ---- Run ----
run:
	.venv/bin/python main.py

# ---- Testing ----
test:
	.venv/bin/python -m pytest -vvs src/tests/ -s

# ---- Code Checks ----
pre-commit:
	pre-commit run --all-files

static-type-checks:
	.venv/bin/python -m mypy .