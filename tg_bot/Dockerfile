FROM python:3.12-alpine

WORKDIR /code

COPY . .

RUN python -m pip install pip --upgrade
RUN pip install -r requirements.txt


CMD ["python", "tg_bot.py"]