# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN pip install awscli

COPY requirements/common.txt /opt/pip/requirements/common.txt
RUN pip install -r /opt/pip/requirements/common.txt

COPY requirements/test.txt /opt/pip/requirements/test.txt
RUN pip install -r /opt/pip/requirements/test.txt

ADD . /opt/app
WORKDIR /opt/app

EXPOSE 8000
#CMD ["python", "manage.py", "runserver"]
