web: gunicorn saferasoft.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
