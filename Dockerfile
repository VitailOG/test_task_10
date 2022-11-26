FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY r.txt .

RUN apk update \
    && apk add gcc python3-dev musl-dev

RUN pip install --no-cache-dir --upgrade pip && pip install -r r.txt

COPY . .
