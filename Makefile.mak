setup:
	pip install -r requirements.txt

run:
	python run.py "Analyze ROAS drop"

test:
	pytest tests/

lint:
	flake8 src/
