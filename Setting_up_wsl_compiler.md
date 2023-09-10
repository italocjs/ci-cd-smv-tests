run wsl on terminal to start instance at current location.

need to run 

```shell
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install gcc build-essential 
italocjs@ITALODELLG5:/mnt/c/Users/italo/OneDrive/personal_cicd_projects/ci-cd-smv-tests/tools/cpputest$ sudo apt install -y build-essential autoconf automake libtool
```

To test go to root folder and run:
make


```shell
italocjs@ITALODELLG5:/mnt/c/Users/italo/OneDrive/personal_cicd_projects/ci-cd-smv-tests$ make
cc -I./src/average -Wall -c src/average/average.c -o src/average/average.o
cc  ./src/main.o  ./src/average/average.o -o ./app.elf 
```

To run file
```shell
italocjs@ITALODELLG5:/mnt/c/Users/italo/OneDrive/personal_cicd_projects/ci-cd-smv-tests$ ./app.elf
Average: 3.000000
```


To build the cpptest tools, run the following commands:
```shell
italocjs@ITALODELLG5:/mnt/c/Users/italo/OneDrive/personal_cicd_projects/ci-cd-smv-tests/tools/cpputest$ autoreconf -i
italocjs@ITALODELLG5:/mnt/c/Users/italo/OneDrive/personal_cicd_projects/ci-cd-smv-tests/tools/cpputest$ ./configure
italocjs@ITALODELLG5:/mnt/c/Users/italo/OneDrive/personal_cicd_projects/ci-cd-smv-tests/tools/cpputest$ make
```


The docker file can run and make the test automatically, download dependencies and run the test.
```shell
italocjs@ITALODELLG5:/mnt/c/Users/italo/OneDrive/personal_cicd_projects/ci-cd-smv-tests$ docker build -t unit-tests-image -f Dockerfile .
```