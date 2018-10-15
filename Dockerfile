FROM python:3.6-slim
MAINTAINER Alex Stone <alexander-l-stone@gmail.com>

ENV PROJECT_ROOT /web
WORKDIR $PROJECT_ROOT

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:8000