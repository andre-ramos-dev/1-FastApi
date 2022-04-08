# Pull base image
FROM python:3.9.2

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update --fix-missing
RUN apt-get install -y \
    python-pip \
    python-dev \
    libpq-dev \
    gettext \
    libreadline-dev \
    libssl-dev \
    libjpeg-dev \
    libfreetype6-dev \
    binutils \
    libproj-dev \
    gdal-bin \
    postgis

# CleanUp to Save space
RUN apt-get autoclean -y \
    clean -y \
    autoremove -y

# UPDATE/UPGRADE PIP
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

RUN mkdir /code

ADD . /code

WORKDIR /code

RUN pip3 install -r requirements/local.pip


EXPOSE 8000
CMD ["python", "main.py"]

WORKDIR /code