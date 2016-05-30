
FROM ubuntu:latest	
MAINTAINER Andrew Lane / Nathan	

RUN apt-get update -y && apt-get install -y --force-yes git python

WORKDIR /
RUN mkdir pydemo && cd /pydemo
RUN git clone https://github.com/theandrewlane/Docker-POC
RUN cd .. && mkdir yougetdemo && cd /yougetdemo
RUN git clone https://github.com/soimort/you-get.git
RUN cd .. && mkdir /demo-directory
VOLUME /demo-directory
