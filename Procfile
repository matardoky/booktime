release: pipenv run python manage.py migrate
web: daphne -p $PORT --bind 0.0.0.0 -v2 booktime.asgi:application
