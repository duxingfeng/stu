# docker

docker 配置文件 docker/daemon.json  
{   
"graph":"/data/docker",   
"storage-driver":"overlay2",    
"insecure-registries": ["registry.access.redhat.com"."quay.io"],      
"registry-mirrors": ["https://xxsxxo8z.mirror.aliyuncs.com"],      
"bip": "172.7.5.0/24",#根据宿主机的ip进行配置   
"exec-opts": ["native.cgroupdriver=systemd"],   
"live-restore": true    
}

### 镜像

- 镜像的结构：${registry_name}/${repository_name}/${image_name}:${tag_name}
- docker版本信息：docker version
- docker系统信息：docker info
- 启动第一个容器：docker run hello-world
- 登录docker：docker login docker.io
- 搜索：docker search alpine
- 下载镜像：docker pull alpine
- 拉取指定版本镜像：docker pull alpine:3.10.1
- 列出本地镜像：docker images
- 给镜像打标签：docker tag 965ea09ff2ed docker.io/{oldboy1103}/alpine:v3.10.3
- 推送镜像：docker push docker.io/{oldboy1103}/alpine:v3.10.3
- 删除镜像：docker rmi docker.io/{oldboy1103}/alpine:latest
- 查看镜像创建历史：docker history
- 将当前系统中的文件复制到容器中：docker cp

### 容器

- 查看本地容器进程：docker ps -a（运行状态）
- 启动容器（运行镜像）：docker run
- 命令格式：docker run [OPTIONS] IMAGE [COMMAND] [ARG..]
- -i：表示启动一个可交互的容器，并持续打开标准输入
- -t：表示使用终端关联到容器的标准输入输出上
- -d：表示将容器放置后台运行
- --rm：退出后即删除容器
- --name：表示定义容器唯一名称
- IMAGE：表示要运行的镜像
- COMMAND：表示启动容器时要运行的命令
- 交互式启动一个容器：docker run -it lodboy1103:v3.10.3 /bin/sh
- 后台运行：docker run -d ubuntu:17.10 /bin/sh
- 运行镜像：docker run -it centos:7 /bin/bash
- 查看宿主机进程：ps aux|grep sleep|grep -v grep
- 进入容器：docker exec -it 9fb6ac28fa09 /bin/bash
- 停止运行容器：docker stop <container_id>
- 开始运行容器：docker start <container_id>
- 重启容器：docker restart <container_id>
- 删除容器：docker rm <container_id>
- for i in `docker ps -a|grep -i exit|awk '{print $1}'`;do docker -rm -f $i;done

- 提交容器：docker commit -p myalpine oldboy1103/alpine:v3.10.3_with_1.txt

- 导出镜像：docker save <container_id- - alpine_with_1.txt.tar
- 导入镜像：docker load < ./alpine_with_1.txt.tar
- 查看容器运行的日志：docker logs -f <container_id>
- 查看容器内文件结构：docker diff <container_id>
- docker pull nignx:1.12.2
- 映射端口：docker run -p 容器外端口:容器内端口
- docker tag dfc538073c53 feng/nginx:v1.12.2
- docker run --rm --name mynginx -d -p 81:80 feng/nginx:v1.12.2

- 挂载数据卷：docker run -v 容器外目录:容器内目录
- mkdir html
- wget www.baidu.com -O index.html
- docker run --rm --name nginx_with_baidu -d -p 82:80 -v /root/html:/usr/share/nginx/html feng/nginx:v1.12.2
- 查看容器/镜像的元信息：docker inspect <container_id>

- 传递环境变量
- docker run -e 环境变量key=环境变量value
- 容器网络：docker network XXXX
- 容器内安装软件（工具）
- yum/apt-get/apt
- tee /etc/apt/sources.list << EOF
- deb http://mirrors.163.com/debian/ jessie main non-free contrib
- deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib
- EOF
- apt-get update && apt-get install curl -y
- docker commit -p <container_id> feng/nginx:curl
- docker push feng/nginx:curl

### docker-compose

- 查看版本：docker-compose version
- 查看配置：docker-compose config
- 后台启动：docker-compose up -d
- 构建镜像：docker-compose build
- 下载镜像：docker-compose pull
- 运行的：docker-compose ps
- 进程：docker-compose top
- 启动：docker-compose start
- 停止：docker-compose stop

### Dockerfile

- Dockerfile的规则：
- 格式：
- -# 为注释
- 指令（大写）内容（小写）

- 忽略文件：.dockerignore
- 指定文件：docker build -f
- 添加标签：docker build -t
- 不使用缓存：docker build --no-cache
- 构建时变量：docker build --build-arg


- Docker是按顺序执行Dockerfile里的指令集合的（从上到下依次执行）
- 每一个Dockerfile的第一个非注释行指令，必须是"FROM"指令，用于为镜像文件构建过程中，指定基准镜像，后续的指令运行于此基准镜像所提供的运行环境中
- 实践中，基准镜像可以是任何可用镜像文件，默认情况下，docker build会在docker主机（本地）上查找指定的镜像文件，当其在本地不存在时，则会从Docker registry（远端）上拉取所需镜像文件。

- 4组核心的Dockerfile指令
- USER/WORKDIR
- USER：使用nginx用户
- WORKDIR：下面的操作在此目录下进行工作
- ADD/EXPOSE
- ADD ：将文件放到镜像中
- EXPOSE:对外暴露的端口，运行容器时，使用-P参数(随机生成端口号)
- RUN/ENV
- ENV：环境变量
- RUN：构建镜像时执行可执行的命令
- CMD/ENTRYPOINT

- 例子：
- Dockerfile文件：
- FROM docker.io/feng/nginx:v1.12.2
- USER nginx  <!--使用nginx用户--->
- WORKDIR /usr/share/nginx/html  <!--在此目录下进行工作--->

- docker build . -t docker.io/feng/nginx:v1.12.2_with_user_workdir

### 工具平台
- 混沌工程：chaosblade
- 覆盖率：AMS
- 代码审计平台 sonar
- 图数据库neo4j、echarts