# Docker Proof Of Concept Demo - ```CS3750```

![Docker](https://upload.wikimedia.org/wikipedia/commons/7/79/Docker_(container_engine)_logo.png?raw=true)

#### This Dockerfile uses ```apt-get``` to install Python 3 and Git. After the install, it uses Python's ```pip``` to install an application called ```you-get```. This demo will execute a Python script (executing various sorting algorithms), and download media from ```you-get``` to the host directory created in step 5. 

<hr>
### Commands used for demo:
#### Host Machine:
1.  ```docker --version```
2. ```sw_vers```
  - Show the current running OS
3. ```git clone https://github.com/theandrewlane/Docker-POC``` 
  - Clone this repository which contains the dockerfile and also a .py script
4. ```cd Docker-POC```
5. ```mkdir docker-shared-files``` 
  - Create a directory to share with the container
6. ```docker build -t docker-class-demo:latest .```
  - Build the docker container (docker-class-demo) using the latest dockerfile
7. ```sw_vers```
  - Show the current running OS
<hr>

#### Docker Container:

1. ```docker run -t -i -v ~/Desktop/docker-shared-files://demo-directory docker-class-demo /bin/bash``` 
  - Create a docker bin/bash shell, link to shared folder
2. ```cat /etc/lsb-release``` 
  - Show the current running OS
3. ```ls```
  - List the directories
4. ```cd Docker-POC```
5. ```python3 SortingTest.py``` 
  - Execute Python demo program
6. ```you-get -o /demo-directory  'https://www.youtube.com/watch?v=dQw4w9WgXcQ'``` 
  - Execute You-Get Program
