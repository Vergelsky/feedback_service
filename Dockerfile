FROM python:3.12-alpine

WORKDIR /code

COPY ./requirements.txt .

RUN python -m pip install pip --upgrade
RUN pip install -r requirements.txt

COPY . .