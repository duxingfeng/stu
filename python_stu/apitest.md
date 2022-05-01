### TCP与UDP的区别

- TCP：面向连接、错误重传、拥塞控制、适用于可靠性高的场景
- UCP：不需要提前建立连接、实现简单、适用于适时性高的场景

### 协议分析工具

- 安全测试：burpsuite
- 自动化测试：mitmproxy

### curl

- -H : 消息头设置
- -u：用户认证
- -d：要发送的post的数据
- -data-urlencode 'page_size=50' 对内容进行url编码
- -G：把data数据当成get请求的参数发送，
- -o：写文件
- -x：代理http代理
- -v：verbose打印更详细日志
- -s：关闭一些提示输出

### charles

- rewrite：简单mock
- map loacl： 复杂mock
- map remote：整体测试环境

### 网络

- 应用层：http、websocket

### mitmproxy

- 安装：
- pip3 install pipx
- pip3 install mitmproxy

- 使用：
- mitmdump
- 设置代理
- 证书：mitm.it

### 模版技术

- mustache
- import pystache

### 压测工具

- Locust
- nGrinder

### 安全

- 模拟安全测试的环境：DVWA
- 安全的机构：owasp.org
- 安全工具：OWASP ZAP（入手）、WVS、AppScan、BurpSuite、Sqlmap

### 性能测试

- 插件：locust
