web: daphne realtime_project.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker --settings=realtime_project.settings
