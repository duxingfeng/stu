# kubetcl 工具

### 管理k8s核心资源的三种基本方法：

#### 陈述式管理方法——主要依赖命令行CLI工具进行管理
- 查看名称空间：kubectl get namespaces
- 查看名称空间内的资源：kubectl get all -n default
- 创建名称空间：kubectl create namespace app
- 删除名称空间：kubectl delete namespace app
- 创建deployment：kubectl create deployment nginx-dp --image=harbor.od.com/public/nginx:v1.7.9 -n kube-public
- 查看deployment：
    - 简单查看：kubectl get deploy -n namespace
    - 扩展查看：kubectl get deploy -n namespace -o wide
    - 详细查看：kubectl describe deployment nginx-dp -n namespace
- 查看pod资源：kubectl get pods 
- 进入pod资源：kubectl exec -it nginx-dp /bin/bash -n namespace
- 删除(重启)pod资源：kubectl delete pod nginx-dp -n namespace
    - 强制删除 --force --grace-period=0
- 删除deployment：kubectl delete deploy nginx-dp -n namespace

#### service

- kubectl expose deployment nginx-dp --port=80 -n namespace
- kubectl scale deployment nginx-dp --replicas=2 -n namespace
- kubectl describe svc nginx-dp -n namespace
- 小结：
    - kubernetes 集群管理集群资源的唯一入口是通过相应的方法调用apiserver的接口
    - kubectl是官方的CLI命令行工具，用于与apiserver 进行通信，将用户在命令行输入的命令，组织并转化为apiserver能识别的信息，进而实现管理k8s各种资源的一种有效途径
    - kubectl 命令大全  
        - kubectl --help
        - http://docs.kubernetes.org.cn
    - 陈述式资源管理方法可以满足90%以上的资源管理需求，但它的缺点也很明显
        - 命令冗长、复杂、难以记忆
        - 特定场景下，无法实现管理需求
        - 对资源的增、删、查操作比较容易，改就很痛苦

#### 声明式管理方法——主要依赖统一资源配置清单（manifest）进行管理

- 声明式管理方法依赖于——资源配置清单（yaml/json）
    - 查看资源配置清单的方法
        - kubectl get svc nginx-dp -o yaml -n namespace
    - 解释资源配置清单
        - kubectl explain service
    - 创建资源配置清单
        - vi /root/nginx-ds-svc.yaml
    - 应用资源配置清单
        - kubectl apply -f nginx-dp-svc.yaml
    - 修改资源配置清单并应用
        - 在线修改
        - 离线修改
    - 删除资源配置清单
        - 陈述式删除
        - 声明式删除
    - 小结：
        - 声明式资源管理方法，依赖于统一资源配置清单文件对资源进行管理
        - 对资源的管理，是通过事先定义在统一资源配置清单内，再通过陈述式命令应用到k8s集群里
        - 语法格式：kubectl create/apply/delete -f /path/to/yaml
        - 资源配置清单的学习方法：
            - tip1：多看别人(官方)写的，能读懂
            - tip2：能照着现成的文件该着用
            - tip3：遇到不懂的，善用kubetcl explain 。。 查
            - tip4：初学切忌上来就无中生有，自己憋着写
#### GUI式管理方法——主要依赖图形化操作页面（web页面）进行管理
