FROM ubuntu:latest
MAINTAINER Andrew Lane "theeandrewlane@gmail.com"
RUN apt-get update && \
  apt-get install -y python3 git 
  # Define working directory.

RUN git clone https://github.com/soimort/you-get.git /myapp/

RUN cd /myapp &&  python3 ./setup.py install

MOUNT .:/myapp                                

WORKDIR /myapp


# Clean-up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /myapp/

# Define default command.
CMD ["bash"]

