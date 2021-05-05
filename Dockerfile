FROM python:3.6
RUN apt-get update && apt-get install -y \
    pypy3 \
    yarn \
    && pip install pipenv


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /atcoder