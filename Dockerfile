FROM python:3.11-slim

LABEL org.opencontainers.image.source=https://github.com/almazkun/jeonse

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

#RUN apt-get update && apt-get install gettext -y

COPY ./Pipfile ./Pipfile.lock ./

RUN pip3 install pipenv gunicorn && pipenv install --system

#COPY apps ./apps
COPY jeonse ./jeonse
#COPY locale ./locale
COPY settings ./settings
COPY static ./static
COPY templates ./templates
COPY manage.py ./

ENTRYPOINT [ "gunicorn" ]

CMD [ "--bind", "0.0.0.0:8000", "settings.wsgi:application", "--reload", "-w", "2", "--access-logfile", "-" ]
