FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /challenge
WORKDIR /challenge
COPY requirements.txt /challenge/
RUN pip install -r requirements.txt
COPY . /challenge/

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB scoredb

COPY init.sql /docker-entrypoint-initdb.d/
