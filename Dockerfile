FROM python:3
ENV PYTHONUNBUFFERED 1

ENV TZ=Asia/Almaty
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir -p /kazdream /kazdream/static

# Installing dependencies
RUN apt-get update

WORKDIR /kazdream
COPY requirements.txt /kazdream/
RUN pip install -r requirements.txt
COPY . /kazdream/
