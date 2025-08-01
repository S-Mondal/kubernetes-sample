FROM python:3.11-slim

LABEL maintainer='Souvik Mondal'
LABEL email=mondalsouvik480@gmail.com

ARG directory

WORKDIR /app
COPY .dockerignore .
COPY ./$directory .

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "app.py"]