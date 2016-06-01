# Docker-POC - CS3750

### This Dockerfile uses ```apt-get``` to install Python 3 and Git. This demo runs a python script and a python program for downloading videos. 

Commands used for demo:
## Host
- ```docker --version```
- ```sw_vers```
- ```git clone https://github.com/theandrewlane/Docker-POC```
- ```cd Docker-POC```
- ```mkdir docker-shared-files```
- ```docker build -t docker-class-demo:latest .```
- ```sw_vers```  
<hr>

## Container

- ```docker run -t -i -v ~/Desktop/docker-shared-files://demo-directory docker-class-demo /bin/bash```
- ```cat /etc/lsb-release```
- ```ls```
- ```cd Docker-POC```
- ```python3 SortingTest.py```
- ```you-get -o /demo-directory  'https://www.youtube.com/watch?v=dQw4w9WgXcQ'```
