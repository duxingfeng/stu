#pytest

> pytest和python解释器运行pytest框架的测试用例方式方法：      
> 1.文件路径  pytest自动能找到test_的文件    
> 2.运行执行方式，main方法

> 常用参数:   
> 1.-k：满足表达式的都会执行  pytest -k "add or div"    
> 2.--collect_only 只负责收集测试用例    
> 3.-m 加标签，执行需要加个-m参数   
> 4.-junit-xml 生成一个执行结果的xml文件   

> conftest.py文件  
> 可以共享数据，方法，fixture方法放置在这个文件下，fixture方法需要传入方法里执行，除非使用autoUse=True      
> 改写方法，改写执行顺序  
> 改写方法，自动添加标签

> 执行顺序：pytest-ordering  
> @pytest.mark.run(order=1)

> pytest.ini配置文件中   
>   可以修改读取文件的规则（以test_开头）    
> pytest_files  
> pytest_classes
> pytest_functions

> 导出依赖包：    
> pip freeze > requirements.txt  
> pip install -r requirements.txt

> 浮点数精度问题：decimal

> fixture：  
> yield 生成器，相当于return+ 暂停+记录上一次的运行位置，与fixture结合使用，激活yield后面的操作  
> 执行顺序：session>module>function ,如果有autouse=True，级别大于同等级

> 工厂模式  

> 反射:hasattr():判断实例有没有属性或者方法
>   getattr()：获取实例的属性或者方法
> 

> 多线程并行与分布式执行:  
> pytest-xdist
> 
> 读取yaml文件：
> pyyaml safe_load(open("yaml_fail""))
> 
> allure    
> 测试数据：--alluredir=./result/(这个选项用于指定存储测试结果的路径)  
> 查看测试报告：
>> 一：allure serve ./result/      
>> 二：生成报告：allure generate ./result/  --clean(注意：覆盖路径加--clean)
>     打开报告：allure open -h 127.0.0.1 -p(启动一个端口) ./result/
> 
> 测试用例顺序：pytest-ordering
> 
> 