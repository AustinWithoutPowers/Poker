init: ./requirements.txt
	pip install -r ./requirements.txt

run: ./src/main.py
	python.exe -m src.main

unit_test: ./tests/unit_tests.py
	python.exe -m tests.unit_tests