release: python manage.py migrate
web: daphne booktime.asgi:application -p $PORT --bind 0.0.0.0 -v2