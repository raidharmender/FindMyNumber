create-venv:
	python3 -m venv .venv

activate-venv:
	. .venv/bin/activate

run:
	python3 src/main.py

test:
	python3 src/testmatrix.py