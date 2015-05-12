TEST_FILES = $(wildcard tests/test_*.py)
TESTS = $(subst .py,,$(subst /,.,$(TEST_FILES)))
VERSION = $(shell cat setup.py | grep version | sed -e "s/version=//" -e "s/'//g" -e "s/,//" -e 's/^[ \t]*//' | tail -1)

all.PHONY: tox_test

tox_test:
	@echo "Running python tox tests"
	@tox

install:
	@echo "Creating distribution package for version $(VERSION)"
	@echo "-----------------------------------------------"
	python setup.py sdist
	@echo "Installing package using pip"
	@echo "----------------------------"
	pip install --upgrade dist/configparser2-$(VERSION).tar.gz

coverage:
	@tox
	@coverage report
