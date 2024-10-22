build-window:
	pyinstaller --onefile --windowed main.py

build-linux:

run:
	python main.py

init:
	pip install pygame configparser
