# Linux

> uname -a: 查看Linux内核版本

> cat /etc/redhat-release: 查看linux版本    
> getenforce    
> 关闭firewalld：systemctl stop firewalld   
> free -m

> 安装epel源/base源：curl -o /etc/yum.repos.d/Centos-Base.repo http://mirrots.aliyun.com/repo/Centos-7.repo    
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

> 设置主机名称：hostnamectl set-hostname hdss7-21.host.com   
> 修改网络信息：vi /etc/sysconfig/network-scripts/ifcfg-etc0   
> 重启网络：systemctl restart network

> 安装必要工具：yum install wget net-tools telnet tree nmap sysstat lrzsz dos2unix bind-utils -y   
> 查看域名的ip地址：nslookup www.qq.com  
> 安装bind9 软件： yum install bind -y   
> 查看bind 版本：rpm -qa bind    
> 修改bind配置文件-主配置文件：vi /etc/named.conf 
>> listen-on port 53 { 10.4.7.11; };    
>> allow-query { any; };    
>> forwarders { 10.4.7.254; };    
>> recursion yes;   
>> dnssec-enable no;     
>> dnssec-validation no;    
> 
> 检查配置情况: named-checkconf
>
> 区域配置文件