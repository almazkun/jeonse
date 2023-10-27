FROM python:3.12-slim

LABEL org.opencontainers.image.source=https://github.com/almazkun/jeonse

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./Pipfile ./Pipfile.lock ./

RUN pip3 install pipenv daphne && pipenv install --deploy --ignore-pipfile --system

COPY jeonse ./jeonse
COPY settings ./settings
COPY static ./static
COPY templates ./templates
COPY manage.py ./

ENTRYPOINT [ "daphne" ]

CMD [ "settings.asgi:application", "-b", "0.0.0.0", "-p", "8000" ]