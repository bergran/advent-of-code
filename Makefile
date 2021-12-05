tests:
	python -m pytest --cov --cov-report=term-missing

execute:
	PYTHONPATH=`pwd` python $(YEAR)/$(DAY)/main.py