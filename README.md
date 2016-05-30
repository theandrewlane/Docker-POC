# Docker-POC - CS3750

### This Dockerfile uses ```apt-get``` to install Python 3 and Git. This demo runs a python script and a python program for downloading videos. 

Commands used for demo:

1. ```docker --version```
  
2. ```sw_vers```

3. ```git clone https://github.com/theandrewlane/Docker-POC```

4. ```cd Docker-POC```

4. ```mkdir docker-shared-files```

5. ```docker build -t docker-class-demo:latest .```

6. ```sw_vers``` 

7. ```docker run -t -i -v ~/Desktop/docker-shared-files://demo-directory docker-class-demo /bin/bash```

8. ```cat /etc/lsb-release```

9. ```ls```

10. ```cd Docker-POC```

11. ```python3 SortingTest.py```

12. ```you-get -o /demo-directory  'https://www.youtube.com/watch?v=dQw4w9WgXcQ'```
