
FROM ubuntu:latest	
MAINTAINER Andrew Lane / Patrick Jenson	

RUN apt-get update -y && apt-get install -y --force-yes git python3 python3-setuptools
RUN easy_install3 pip

WORKDIR /
RUN mkdir pydemo && cd /pydemo
RUN git clone https://github.com/theandrewlane/Docker-POC
VOLUME /demo-directory
