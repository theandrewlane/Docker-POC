
#Grab the latest ubuntu image
FROM ubuntu:latest	
MAINTAINER Andrew Lane / Patrick Jenson	

#Install required programs
RUN apt-get update -y && apt-get install -y --force-yes git python3 python3-setuptools
RUN easy_install3 pip
RUN pip3 install you-get

# Set the locale
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

#Set working directory, make demo folders, and intstall software
WORKDIR /
RUN mkdir pydemo && cd /pydemo
RUN git clone https://github.com/theandrewlane/Docker-POC
VOLUME /demo-directory
