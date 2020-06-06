FROM python:3.8.2-alpine

ENV HOME=/usr/src/api
WORKDIR $HOME

# general libs
RUN apk update && apk add python3-dev gcc build-base

# libs for lxml
RUN apk add libxml2 libxslt libxslt-dev

# libs for postgresql
RUN apk add postgresql-dev

RUN pip install setuptools --upgrade pip

COPY ./requirements.txt .
COPY . $HOME
RUN pip install --no-cache-dir -r requirements.txt

RUN flake8 --ignore=E501,F401,F403,E402 .

# EXPOSE 8080

# CMD uvicorn main:app --reload --host 0.0.0.0 --port 8080
