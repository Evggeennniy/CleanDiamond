setup:
	sudo apt install python3 &&
	sudo apt install python3-pip &&
	sudo apt install python3-venv &&
	source ./venv/bin/Activate &&
	pip install requirements.txt &&
	python app/manage.py makemigrations &&
	python app/manage.py migrate &&
	python app/manage.py runserver