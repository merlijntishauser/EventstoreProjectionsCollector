FROM ubuntu:trusty
MAINTAINER Psybizz B.V. <development@psybizz.eu>

# Set locale
RUN locale-gen --no-purge en_US.UTF-8
ENV LC_ALL en_US.UTF-8


ENV DEBIAN_FRONTEND noninteractive

# update packages and install base packages
RUN apt-get update && apt-get install -yq \
wget \
locate \
python-pip \
python-dev \
build-essential \
python-software-properties \
net-tools \
pbuilder \
python-mock \
python-configobj \
python-support \
cdbs \
inetutils-ping \
curl

# install dependencies for diamond by pip
RUN pip install --upgrade pip
RUN pip install --upgrade virtualenv
RUN pip install psutil

# install diamond
RUN pip install diamond>3.5

# install rabbitMQ python Library
# http://pyrabbit.readthedocs.org/en/latest/
RUN pip install PyRabbit>1.1

# create log directory
RUN mkdir /var/log/diamond

# copy diamond handlers configuration
ADD handlers/ArchiveHandler.conf /etc/diamond/handlers/ArchiveHandler.conf

# copy collectors configuration


# copy configuration
ADD config/diamond.conf  /etc/diamond/diamond.conf
