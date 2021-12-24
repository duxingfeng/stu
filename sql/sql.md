# 查询

-----
### 基本查询
> 排序查询: select * from table_name order by b desc;
>
> 分页: select * from table_name limit 0,10;
>
> 去重: select distinct gender from employees;

### 条件查询
> 比较：等于= &emsp;&emsp;大于> &emsp;&emsp;小于< &emsp;&emsp;不等于<>
> 
> 通配：where CustomerName like "%or%";
>
> 范围限定: where Price between 10 and 20;
> 
> 子集限定: where Country in ('Germany','France','UK');
> 
> 逻辑关系: and or not

#### 聚合查询
> 基本语法：group by 字段 having 条件 
> 
> 常用函数：count，max，min，sun，avg

#### sql 查询思维方式：   
> 1。分析查询需求的查询结果和限制条件    
> 2。结合表结构分析查询结果和限制条件对应的表或字段  
> 3。如果查询结果和限制条件在同一个表，则为单表查询，否则为多表查询  
> 4。结合sql基础知识和对表结构的熟悉，应用sql查询思维编写sql语句

#### 索引
> 分类：   
> 1。主键索引    
> 2。唯一索引    
> 3。普通索引    
> 4。全文索引    
> 5。组合索引    

