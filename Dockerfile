FROM python:3.7.1-alpine
MAINTAINER Pierre-Henri Bourdeau <phbasic@gmail.com>

RUN apk --no-cache add openssl-dev
RUN apk --no-cache add --virtual \
    build-dependencies \
    gcc \
    g++ \
    make \
    libffi-dev \
    libxslt-dev \
    py-gunicorn

COPY . /app
WORKDIR /app

RUN pip3 install pipenv gunicorn
RUN pipenv install --system --deploy --ignore-pipfile


RUN cp ./config-dist.py config.py

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "--reload", "wsgi:app" ]
