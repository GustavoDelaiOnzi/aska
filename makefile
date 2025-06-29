# Define variables
VERSION := 3.13.3
PROJECT:= aska
VENV := $(PROJECT)-$(VERSION)
PYTHON_BIN = $(shell pyenv root)/versions/$(VENV)/bin
TWINE := $(PYTHON_BIN)/twine
PIP = $(PYTHON_BIN)/pip
PYTHON = $(PYTHON_BIN)/python3

.PHONY: create-venv
create-venv:
	pyenv install -s $(VERSION)
	pyenv uninstall -f $(VENV)
	pyenv virtualenv $(VERSION) $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install .[dev]

.PHONY: test
test:
	 pytest --cov=project --cov-report=term-missing:skip-covered --cov-fail-under=100 --color=yes --durations=10

.PHONY: clean
clean:
	rm -rf __pycache__/ build/ dist/ *.egg-info .pytest_cache .coverage
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name "*.log" -delete

.PHONY: code-convention
code-convention:
	pre-commit run --all-files

.PHONY: code-convention
run-rabbit:
	@docker start rabbitmq 2>/dev/null || docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

ch:
	cz ch
	git add CHANGELOG.md
	git commit --amend --no-edit

c:
	cz c
	cz ch
	git add CHANGELOG.md
	git commit --amend --no-edit