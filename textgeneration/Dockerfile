FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/
RUN pip install -r req.txt

CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin', '543678')" \
    && python manage.py collectstatic --no-input \
    && gunicorn textgeneration.wsgi:application --bind 0.0.0.0:8000