# Linux

> uname -a: 查看Linux内核版本

> cat /etc/redhat-release: 查看linux版本    
> getenforce    
> systemctl stop firewalld   
> free -m
>
> curl -o /etc/yum.repos.d/Centos-Base.repo http://mirrots.aliyun.com/repo/Centos-7.repo
> yum install epel-release -y
> yum list docker --show-duplicates
> yum install -y yum-utils
> yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
> yum list docker-ce --show-duplicates
> yum install docker-ce
> systemctl enable docker
> systemctl start docker
> mkidr /etc/docker
> vi /etc/docker.daemon.json