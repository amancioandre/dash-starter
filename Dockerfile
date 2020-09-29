FROM python:3.7-slim as development
WORKDIR /usr/src/dashboard
COPY ./requirements.txt .
RUN pip install -r requirements.txt