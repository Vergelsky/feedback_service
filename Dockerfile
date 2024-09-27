FROM python:3.12-alpine

WORKDIR /code

COPY ./requirements.txt .

RUN apk update && apk add --no-cache dcron bash

RUN python -m pip install pip --upgrade && pip install -r requirements.txt

COPY . .

COPY ./cronjob /etc/crontabs/root
RUN chmod 0644 /etc/crontabs/root
