# These must be run inside a venv created in this folder.
# MUST BE USED RUN AFTER venv\Scripts\activate

install:
	pip install -r requirements.txt

run:
	python manage.py runserver

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

createsuperuser:
	python manage.py createsuperuser

collectstatic:
	python manage.py collectstatic --noinput

shell:
	python manage.py shell

test:
	python manage.py test