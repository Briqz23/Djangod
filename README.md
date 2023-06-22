# Djangod

pipenv install django
pipenv shell
django-admin startproject djangod . 
python manage.py runserver 8000

config vscode:
ctrl shift p -> selct interpreter -> conteúdo de pipenv --venv/bin/venv
source <PATH>/bin/activate 
pipenv install django-debug-toolbar (configurar - ler docs)
python manage.py runserver
python manage.py startapp playground
