FROM python:3.8

WORKDIR /usr/src/app

ENV FLASK_APP=app.py

COPY ./app /usr/src/app

RUN mkdir -p logs

RUN pip install --upgrade pip
RUN pip install -r requirements.txt