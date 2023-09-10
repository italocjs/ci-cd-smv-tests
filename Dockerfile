# Fetch ubuntu 22.04
FROM ubuntu:22.04

#install python on image,  \ is used to break the line 
RUN \
    apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y build-essential

# create a directory for out test files 
RUN mkdir /tests

# copy in our python script
COPY test.py /tests/test.py

# copy in our c file
COPY main.c /tests/main.c

# command that wull run when the container starts
ENTRYPOINT ["python3", "/tests/test.py"]
#CMD ["something", "else"] # pass this as an argument to the entrypoint

