FROM python:3.12-alpine

WORKDIR /code

COPY ./requirements.txt .

RUN apk add --no-cache gcc musl-dev linux-headers libffi-dev openssl-dev \
    && apk add --no-cache bash \
    && apk add --no-cache dcron



RUN python -m pip install pip --upgrade
RUN pip install -r requirements.txt

COPY . .

COPY ./cronjob /etc/crontabs/root
RUN chmod 0644 /etc/crontabs/root

CMD dcron
