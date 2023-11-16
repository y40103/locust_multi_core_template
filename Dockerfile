FROM python:3.10-bullseye

RUN mkdir /app
RUN mkdir /locust
COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

