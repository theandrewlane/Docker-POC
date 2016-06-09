# Docker-POC - CS3750

### This Dockerfile uses ```apt-get``` to install Python 3 and Git. This demo runs a python script and a python program for downloading videos. 

Commands used for demo:
## Host
- ```docker --version```
- ```sw_vers```
-- #Show the current running OS
- ```git clone https://github.com/theandrewlane/Docker-POC``` 
-- #Clone this repository which contains the dockerfile and also a .py script
- ```cd Docker-POC```
- ```mkdir docker-shared-files``` 
-- #Create a directory to share with the container
- ```docker build -t docker-class-demo:latest .```
-- #Build the docker container (docker-class-demo) using the latest dockerfile
- ```sw_vers```  
-- #Show the current running OS
<hr>

## Container

- ```docker run -t -i -v ~/Desktop/docker-shared-files://demo-directory docker-class-demo /bin/bash``` 
-- #Create a docker bin/bash shell, link to shared folder
- ```cat /etc/lsb-release``` 
-- #Show the current running OS
- ```ls```
-- #List the directories
- ```cd Docker-POC```
- ```python3 SortingTest.py``` 
-- #Execute Python program
- ```you-get -o /demo-directory  'https://www.youtube.com/watch?v=dQw4w9WgXcQ'``` 
-- #Execute You-Get Program
