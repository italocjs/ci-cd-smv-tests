# Basic guide to get docker and github actions to test c/python code

Full guide:
- part 1: https://youtu.be/1nxGcfIm-TU
- part 2: https://www.youtube.com/watch?v=8pyqbYDYkRs
- part 3: https://www.youtube.com/watch?v=lZWFmEhIhpY

- Github: https://github.com/ShawnHymel/c-unit-test

## Docker setup
- **building image**

    ```shell
    docker build -t my-image .
    ```
    - i flag = interactive mode, if it should keep running and have terminal interaction.
    - t --entrypoint="/bin/bash" = will use bash?
    - . means the dockerfile is in the current directory, if not used, full path must be specified
   

- **building container**

    ```shell
    docker create -i -t --entrypoint="/bin/bash" --name my-container my-image # Create container from image, run bash, keep STDIN open
    ```

- **copy file** from host to container (file deleted after container is stopped)

    ```shell
    docker cp another-test.py my-container:/home/another-test.py

    PS D:\HelloDocker> docker create -i -t --entrypoint="/bin/bash" --name my-container my-image
        f6ba99d10ffea832cd60f0b6720bc651fd103d24844ffe8b8eb19dd938d88747
    ```
- **start container**, keep interactive mode

    ```shell
    docker start -i my-container

    PS D:\HelloDocker> docker start -i my-container
        root@f6ba99d10ffe:/# 
    ```


- **exit container: **   
    ```shell
    exit
    ```

- **remove container**
    ```shell
    docker rm my-container
    ```

- **lists all containers**
    ```shell
    docker container ls -a
    ```

- **start specific container from list**
    ```shell
    PS D:\HelloDocker> docker container ls -a
        CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS    PORTS     NAMES
        e2bc96c92115   my-image   "python3 /tests/test…"   23 seconds ago   Created             laughing_shaw
    PS D:\HelloDocker> docker start -i laughing_shaw
        Hello World!
    PS D:\HelloDocker> docker container rm laughing_shaw  
    laughing_shaw
    PS D:\HelloDocker> docker container ls -a
    CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
    ```

- **create, run, delete container**

    ```shell
    PS D:\HelloDocker> docker run --rm my-image
    Hello World!
    PS D:\HelloDocker> docker container ls -a
    CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
    PS D:\HelloDocker> 
    ```

- **delete an image** (all containers must be deleted first)

    ```shell
    PS D:\HelloDocker> docker image rm my-image
    Untagged: my-image:latest
    Deleted: sha256:9b20eacf3e1e5aeb255694e4daed5a6fd04d5be676ac5d1e9b0cc90613f62943
    PS D:\HelloDocker> docker image ls -a
    REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
    PS D:\HelloDocker> 
    ```

## Unit testing
- Stub: predefined return for interface 
- Mock: prefefined behavior for interaction
- Fake: limited working implementation

