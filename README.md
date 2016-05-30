# Docker-POC - CS3750

### This Dockerfile uses ```apt-get``` to install Python 3 and Git. This demo runs a python script and a python program for downloading videos. 

Commands used for demo:

1.  ```docker --version```
  
2.  ```sw_vers```

3.  ```git clone https://github.com/theandrewlane/Docker-POC```

4.  ```cd Docker-POC```

5.  ```mkdir docker-shared-files```

6.  ```docker build -t docker-class-demo:latest .```

7.  ```sw_vers``` 

8.  ```docker run -t -i -v ~/Desktop/docker-shared-files://demo-directory docker-class-demo /bin/bash```

9.  ```cat /etc/lsb-release```

10. ```ls```

11. ```cd Docker-POC```

12. ```python3 SortingTest.py```

13. ```you-get -o /demo-directory  'https://www.youtube.com/watch?v=dQw4w9WgXcQ'```
