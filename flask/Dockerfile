FROM python:3.6-alpine

# This hack is widely applied to avoid python printing issues in docker containers.
# See: https://github.com/Docker-Hub-frolvlad/docker-alpine-python3/pull/13
ENV PYTHONUNBUFFERED=1

ENV WORKDIR=/opt/services/flaskapp/src/
ENV FLASK_APP=app.py


RUN apk -U add vim
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev postgresql-client

RUN mkdir -p ${WORKDIR}
COPY requirements.txt ${WORKDIR}
COPY manage.py ${WORKDIR}
COPY test_db.py ${WORKDIR}
COPY .env ${WORKDIR}
ADD app/ ${WORKDIR}/app

WORKDIR ${WORKDIR}

RUN pip install setuptools==45
RUN pip install -r ./requirements.txt --no-cache-dir

