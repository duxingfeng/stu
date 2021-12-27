# shell

---

## 文件  

> echo:输出内容

---

## 网络  

> ping 测试网络的链接  
>>
>> -c  ping的次数  
>> -l  每次ping的时间间隔
>>
> netstat:打印linux网络系统的状态信息  
>>
>> -t  列出所有tcp  
>> -u  列出所有utp  
>> -l  只显示监听端口  
>> -n  以数字形式显示地址和端口号  
>> -p  显示进程的pid和名字

---

## 性能  

>uptime :有多少用户正在登录
>>result: 23:33  up 2 days,  3:23, 1 user, load averages: 1.62 1.18 1.03  
>>>load averages: 1分钟，5分钟，15分钟的平均负载  
>>
>>平均负载：两个项值的加和，然后算出平均值  
>>>runnable：可运行状态的进程数量（正在运行和等待运行）
>>>uninterruptable：不可中断的进程（等待io的进程）  
>>
>>
>>统计有多少个用户：有多少注册的用户
>>>cat /etc/group ｜wc -l  
>>
>>
>dmesg|tail
>>查看系统日志的信息
>>
>@vmstat 1
>>
>>
>top  
>>-n 获取多次cpu的执行情况，top -n 4 只更新4次  
>>-d 间隔时间，top -4 每隔4秒更新一次
>>-p 获取指定端口的进程的数据，top -p 4444  
>>
>ps  

---

## grep

>-v 显示不被pattern匹配到的行  
>-i 忽略字符大小写  
>-n 显示匹配的行号  
>-c 统计匹配的行数  
>-o 仅显示匹配到的字符串  
>-E 使用ERE，相当于egrep

---

## sed

> sed [-hn..][-e&lt;script&gt;][-f&lt;script文件&gt;][文本文件]  
> script：脚本
>> -h 显示帮助  
>> -n 仅显示script处理后的结果  
>> -e&lt;script&gt; 以选项中指定的script来处理输入的文本文件  
>> -f&lt;script文件&gt; 以选项中指定的script文件来处理输入的文本文件  

---

## awk

> awk 'pattern+action' [filenames]
>> -pattern 正则表达式  
>> -action 对匹配到的内容执行的命令（默认为输出每行内容）  
>> 常用参数
>>> filename awk浏览到文件名  
>>> begin 处理文本之前要执行的操作  
>>> end 处理文本之后要执行的操作  
>>> fs 设置输入域分隔符，等价于命令行-F 选项  
>>> nf 浏览记录到域的个数（列数）  
>>> nr 已读的记录数（行数）  
>>> ofs 输出域分隔符  
>>> ors 输出记录分隔符  
>>> rs 控制记录分隔符  
>>> $0 整条记录  
>>> $1 表示当前行的第一个域  

---

## Linux进阶

---
> 查看当前系统版本：cat /proc/version    
> uname -a  
> curl  
>> get  
>>> -G : 使用get请求  
>>> -d : 指定请求数据  
>>
>> post  
>>>-d :指定post请求体  
>>
>> other  
>>> 保存响应内容：curl -o temp.html <https://www.baidu.com>  
>>> 输出通信的整个过程：curl -v <https://www.baidu.com>  
>>> 不输出错误和进度信息：curl -s <https://www.baidu.com>
>>
>jq:<https://stedolan.github.io/jq/>

---

## 正则表达式  

> 代码  说明  
>>. : 匹配除换行符以外的任意字符  
>>\s : 匹配任意的空白符  
>>\d : 匹配数字  
>>\b : 匹配单词到开始或结束  
>>^ : 匹配字符串的开始  
>>& : 匹配字符串的结束  
>>\* : 表示匹配前边一个字符出现0次或者多次  
>>
>>\+ : 重复一次或更多次  
>>? : 重复零次或一次  
>>{n} : 重复n次  
>>{n,} ; 重复n次或更多次  
>>{n,m} : 重复n到m次  
>>| : 表示或  
