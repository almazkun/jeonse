FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/code

RUN apt-get update && apt-get -y upgrade

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && pipenv install --system 

COPY . .