#   Makefile
#
# license   http://opensource.org/licenses/MIT The MIT License (MIT)
# copyright Copyright (c) 2017, TUNE Inc. (http://www.tune.com)
#

.PHONY: clean version build dist local-dev yapf pyflakes pylint

PACKAGE := pycountry-convert
PACKAGE_PREFIX := pycountry_convert

PYTHON3 := $(shell which python3)
PIP3    := $(shell which pip3)

PY_MODULES := pip setuptools pylint flake8 pprintpp pep8 requests six sphinx wheel python-dateutil

PACKAGE_SUFFIX := py3-none-any.whl
PACKAGE_WILDCARD := $(PACKAGE)-*
PACKAGE_PREFIX_WILDCARD := $(PACKAGE_PREFIX)-*
PACKAGE_PATTERN := $(PACKAGE_PREFIX)-*-$(PACKAGE_SUFFIX)

VERSION := $(shell $(PYTHON3) setup.py version)
WHEEL_ARCHIVE := dist/$(PACKAGE_PREFIX)-$(VERSION)-$(PACKAGE_SUFFIX)

PACKAGE_FILES := $(shell find $(PACKAGE_PREFIX) examples ! -name '__init__.py' -type f -name "*.py")
PACKAGE_ALL_FILES := $(shell find $(PACKAGE_PREFIX) tests examples -type f -name "*.py")
PACKAGE_EXAMPLE_FILES := $(shell find examples ! -name '__init__.py' -type f -name "*.py")
PYFLAKES_ALL_FILES := $(shell find $(PACKAGE_PREFIX) tests examples -type f  -name '*.py' ! '(' -name '__init__.py' ')')

TOOLS_REQ_FILE := requirements-tools.txt
REQ_FILE      := requirements.txt
SETUP_FILE    := setup.py
ALL_FILES     := $(PACKAGE_FILES) $(REQ_FILE) $(SETUP_FILE)

# Report the current package version.
version:
	@echo "======================================================"
	@echo version $(PACKAGE)
	@echo "======================================================"
	@echo $(REQUESTS_MV_INTGS_PKG) $(VERSION)

# Install Python 3 via Homebrew.
brew-python:
	@echo "======================================================"
	@echo brew-python
	@echo "======================================================"
	@echo $(shell which python3)
	brew uninstall -f python3
	@echo $(shell which python3)
	brew update
	brew install python3
	@echo $(shell which python3)
	$(PIP3) install --upgrade $(PY_MODULES)

clean:
	@echo "======================================================"
	@echo clean $(PACKAGE)
	@echo "======================================================"
	rm -fR __pycache__ venv "*.pyc" build/*    \
		$(PACKAGE_PREFIX)/__pycache__/         \
		$(PACKAGE_PREFIX)/helpers/__pycache__/ \
		$(PACKAGE_PREFIX).egg-info/*
	find ./* -maxdepth 0 -name "*.pyc" -type f -delete
	find $(PACKAGE_PREFIX) -name "*.pyc" -type f -delete
	@echo "======================================================"
	@echo delete distributions: $(PACKAGE)
	@echo "======================================================"
	mkdir -p ./dist/
	find ./dist/ -name $(PACKAGE_WILDCARD) -exec rm -vf {} \;
	find ./dist/ -name $(PACKAGE_PREFIX_WILDCARD) -exec rm -vf {} \;

uninstall-package: clean
	@echo "======================================================"
	@echo uninstall-package $(PACKAGE)
	@echo "======================================================"
	$(PIP3) install --upgrade list
	@if $(PIP3) list --format=legacy | grep -F $(PACKAGE) > /dev/null; then \
		echo "python package $(PACKAGE) Found"; \
		$(PIP3) uninstall --yes $(PACKAGE); \
		echo "uninstall package $(PACKAGE)"; \
	else \
		echo "python package $(PACKAGE) Not Found"; \
	fi

site-packages:
	@echo "======================================================"
	@echo site-packages
	@echo "======================================================"
	$(eval PYTHON3_SITE_PACKAGES := $(shell python3 -c "import site; print(site.getsitepackages()[0])"))
	@echo $(PYTHON3_SITE_PACKAGES)

remove-package: uninstall-package site-packages
	@echo "======================================================"
	@echo remove-package $(PACKAGE_PREFIX)
	@echo "======================================================"
	rm -fR $(PYTHON3_SITE_PACKAGES)/$(PACKAGE_PREFIX)*

install: remove-package
	@echo "======================================================"
	@echo install $(PACKAGE)
	@echo "======================================================"
	$(PIP3) install --upgrade pip
	$(PIP3) install --upgrade $(WHEEL_ARCHIVE)
	$(PIP3) freeze | grep $(PACKAGE)

freeze:
	@echo "======================================================"
	@echo freeze $(PACKAGE)
	@echo "======================================================"
	$(PIP3) install --upgrade freeze
	$(PIP3) freeze | grep $(PACKAGE)

fresh: dist dist-update install
	@echo "======================================================"
	@echo fresh completed $(PACKAGE)
	@echo "======================================================"

# Register the module with PyPi.
register:
	$(PYTHON3) $(SETUP_FILE) register

local-dev-editable: remove-package
	@echo "======================================================"
	@echo local-dev-editable $(PACKAGE)
	@echo "======================================================"
	$(PIP3) install --upgrade freeze
	$(PIP3) install --upgrade --editable .
	$(PIP3) freeze | grep $(PACKAGE)

local-dev: remove-package
	@echo "======================================================"
	@echo local-dev $(PACKAGE)
	@echo "======================================================"
	$(PIP3) install --upgrade freeze
	$(PIP3) install --upgrade .
	$(PIP3) freeze | grep $(PACKAGE)

dist: clean
	@echo "======================================================"
	@echo dist $(PACKAGE)
	@echo "======================================================"
	$(PIP3) install --upgrade -r requirements.txt
	hub release create -m "$(PACKAGE_PREFIX)-$(VERSION)-$(PACKAGE_SUFFIX)" v$(VERSION)
	$(PYTHON3) $(SETUP_FILE) bdist_wheel upload
	$(PYTHON3) $(SETUP_FILE) bdist_egg upload
	$(PYTHON3) $(SETUP_FILE) sdist --format=gztar upload
	ls -al ./dist/$(PACKAGE_PREFIX_WILDCARD)

tools-requirements: $(TOOLS_REQ_FILE)
	@echo "======================================================"
	@echo tools-requirements
	@echo "======================================================"
	$(PIP3) install --upgrade -r $(TOOLS_REQ_FILE)

pep8: tools-requirements
	@echo "======================================================"
	@echo pep8 $(PACKAGE)
	@echo "======================================================"
	$(PYTHON3) -m pep8 --config .pep8 $(PACKAGE_ALL_FILES)

pyflakes: tools-requirements
	@echo "======================================================"
	@echo pyflakes $(PACKAGE)
	@echo "======================================================"
	$(PIP3) install --upgrade pyflakes
	$(PYTHON3) -m pyflakes $(PYFLAKES_ALL_FILES)

pylint: tools-requirements
	@echo "======================================================"
	@echo pylint $(PACKAGE)
	@echo "======================================================"
	$(PIP3) install --upgrade pylint
	$(PYTHON3) -m pylint --rcfile .pylintrc $(PACKAGE_ALL_FILES) --disable=C0330,F0401,E0611,E0602,R0903,C0103,E1121,R0913,R0902,R0914,R0912,W1202,R0915,C0302 | more -30

yapf: tools-requirements
	@echo "======================================================"
	@echo yapf $(PACKAGE)
	@echo "======================================================"
	$(PYTHON3) -m yapf --style .style.yapf --in-place $(PACKAGE_ALL_FILES)

lint: tools-requirements
	@echo "======================================================"
	@echo lint $(PACKAGE)
	@echo "======================================================"
	pylint --rcfile .pylintrc $(REQUESTS_MV_INTGS_FILES) | more

flake8:
	@echo "======================================================"
	@echo flake8 $(PACKAGE)
	@echo "======================================================"
	flake8 --ignore=F401,E265,E129 $(PACKAGE_PREFIX)

list-package: site-packages
	@echo "======================================================"
	@echo list-packages $(PACKAGE)
	@echo "======================================================"
	ls -al $(PYTHON3_SITE_PACKAGES)/$(PACKAGE_PREFIX)*

run-example: local-dev
	@echo "======================================================"
	@echo run-example
	@echo "======================================================"
	$(PYTHON3) examples/example_country_convert.py

list:
	cat Makefile | grep "^[a-z]" | awk '{print $$1}' | sed "s/://g" | sort

