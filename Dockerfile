FROM python:3.8-slim

WORKDIR /app

USER root

RUN apt-get -y update && pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/
