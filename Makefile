VENV:=source venv/bin/activate

all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

empty_venv:
	rm -rf venv
	python3 -m venv venv
	$(VENV) && pip install --quiet --upgrade pip
	$(VENV) && pip install --quiet pip-tools

venv: requirements.txt requirements-dev.txt
	$(MAKE) empty_venv
	$(VENV) && pip-sync \
		--quiet \
		requirements.txt requirements-dev.txt
	$(VENV) && pip freeze  # echo the installed lib with their versions

update_requirements:
	# Remove the virtualenv and the requirements lock files
	rm -rf venv requirements.txt requirements-dev.txt
	# Recrete the virtualenv
	$(MAKE) empty_venv
	# Generate the lock file for requirements
	$(VENV) && pip-compile \
		--generate-hashes \
		--allow-unsafe \
		--output-file requirements.txt
	$(VENV) && pip-compile \
		--generate-hashes \
		--allow-unsafe \
		--output-file requirements-dev.txt \
		requirements-dev.in
	# Install all the requirements in the virtualenv
	$(MAKE) venv

run: venv
	FLASK_APP=bamboozler BAMBOOZLER_SETTINGS=../settings.cfg venv/bin/flask run

test: venv
	BAMBOOZLER_SETTINGS=../settings.cfg venv/bin/python -m unittest discover -s tests

sdist: venv test
	venv/bin/python setup.py sdist

########################################################################################
# Lint
########################################################################################

# Run all the linting tools
lint:
	$(VENV) && pre-commit run --all
