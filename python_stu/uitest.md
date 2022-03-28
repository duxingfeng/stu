### 文件上传

- input标签可以直接使用send_keys(文件地址)上传文件

### 弹窗处理

- switch_to.alert():获取当前页面上的警告框
- text：返回alert/confirm/prompt中的文字信息
- accept():接受现有警告框
- dismiss():解散现有警告框
- send_keys(keysToSend):发送文本至警告框

### 拖拽

- ActionChains 模块
- drag_and_drop(drag,drop)
- perform() 执行拖拽

### frame

- switch_to.frame()
- switch_to.default_content()  回到初始的frame

### 使用现有的浏览器，不打开新的浏览器

- 浏览器启动：chrome --remote-debugging-port=92
- Options.debugger_address 参数

### 获取cookie

- driver.get_cookies()

### python自带的小型数据库

- shelve

### windows 截图前置工具

- snipaste

### 等待   

- 隐式等待：self.driver.implicitly_wait()
- 显示等待：WebDriverWait(driver,10).until(expected_conditions.方法)

