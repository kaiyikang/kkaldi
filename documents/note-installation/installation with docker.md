# Installation kaldi by docker

1. installation of docker

https://docs.docker.com/engine/install/ubuntu/

2. installation of nvidia-docker
https://github.com/NVIDIA/nvidia-docker

nvidia/cuda from gitlab: https://gitlab.com/nvidia/container-images/cuda/-/tree/master/dist

```bash
docker pull nvidia/cuda:10.2-base-ubuntu16.04
```

usage:

```bash
docker run --gpus all nvidia/cuda:10.0-base nvidia-smi
```



## docker 使用顺序

~~~bash
# pull nvidia/cuda docker 
sudo docker pull nvidia/cuda:10.2-base-ubuntu16.04

# check ID of image 
sudo docker images

# run image with gpus mode 
sudo docker run --gpus all id
# go-into directly 
sudo docker run -it --gpus all id /bin/bash

# after exit, check stopped container ID
sudo docker ps -a

# start the stopped container 
sudo docker start ID

# reopen it 
sudo docker exec -it ID /bin/bash

# continue installation of Kaldi
~~~

