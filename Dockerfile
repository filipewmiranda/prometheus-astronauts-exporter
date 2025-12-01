FROM python:3.8-slim

LABEL maintainer Filipe Miranda <filipew.mrianda@gmail.com.
LABEL description "Dockerfile para criar umagem de container do nosso primeito exporter"

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt

CMD python3 exporter.py