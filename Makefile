$(eval venvpath     := .venv)
$(eval pip          := $(venvpath)/bin/pip)
$(eval python       := $(venvpath)/bin/python)
$(eval pytest       := $(venvpath)/bin/pytest)

setup-virtualenv:
	@test -e $(python) || python3 -m venv $(venvpath)
	@$(pip) install --quiet --requirement=requirements.txt

test-cpython: setup-virtualenv
	@PYTHONPATH=$(PWD) $(pytest) -vvv tests/test_cpython.py

test-micropython:
	@micropython -c 'import unittest; unittest.main("tests/test_micropython")'

test:

	@echo "=========================================="
	@echo "Running tests on CPython"
	@echo "=========================================="
	@$(MAKE) test-cpython || true
	@echo

	@echo "=========================================="
	@echo "Running tests on MicroPython"
	@echo "=========================================="
	@$(MAKE) test-micropython || true
	@echo
