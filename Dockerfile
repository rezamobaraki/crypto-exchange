FROM ubuntu:latest
LABEL authors="Reza Mobaraki ~ Rezoo"

# Stage 1: Build stage

FROM python:3.12-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install necessary packages, including gettext
RUN apt-get update -o Acquire::Check-Valid-Until=false && \
    apt-get install -y gettext && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /app/

RUN poetry install --no-root

COPY src/ ./

ENV DJANGO_SETTINGS_MODULE=core.settings.django.local

RUN poetry run ./manage.py collectstatic

# Expose port 8000
EXPOSE 8000

# Command to start the server using Gunicorn
CMD ["gunicorn", "--workers=3", "--timeout=600", "--bind=0.0.0.0:8000", "core.wsgi:application"]
