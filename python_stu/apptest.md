### 环境

- jdk
- sdk
- appium desktop
- appium client

### 命令

- adb devices 查看设备是否连接
- 模拟机：网易mumu、 genimotion
- 获取package：adb logcat | grep -i displayed
- 获取当前页面元素：adb shell dumpsys activity top
- 获取任务列表： adb shell dumpsys activity activities

### 测试用例的重要部分

- 导入依赖： from appium import wehdriver
- capabilities 设置

> platformName  
> platformVersion   
> deviceName    
> appPackage    
> appActivity   
> noReset
> 设置输入中文
> unicodeKeyBoard
> resetKeyBoard

### 等待

- 隐式等待(全局性)：

> driver.manage().timeouts().implicitlyWait(10,TimeUnit.SECONDS)   
> 在服务端等待
>

- 显示等待(等待某个元素):

> Element = WebDriverWait(driver,10,0.5).until(expected_conditions.visibility_of_element_located((MobileBy.id,"")))  
> 在客户端等待

### 控件定位与操作

> id    
> classname 多个条件一起定位     
> xpath     
> 工具    
> Uiautomatorviewer

### android基础知识

- 七大布局

> LinearLayout 线性布局  
> RelativeLayout 相对布局   
> FrameLayout 帧布局  
> AbsoluteLayout 绝对布局   
> TableLayout 表格布局  
> GridLayout 网格布局   
> ConstraintLayout 约束布局

- 四大组件

> activity：与用户交互的可视化页面  
> service：实现程序后台运行的解决方案     
> content provider：内容提供者，提供程序所需要的数据      
> broadcast receiver：广播接收器，监听外部事件的到来

- 常用控件

> TextView 文本控件，EditText 可编辑文本控件    
> Button 按钮，ImageButton 图片按钮，ToggleButton 开关按钮
> ImageView 图片控件
> CheckBox 复选框控件，RadioButton 单选框控件

### 触屏操作自动化

- TouchAction

### toast 控件

- 获取手机上的包名：adb shell pm list package
- 截图：save_screenshot
- 录屏工具：scrcpy
- subprocess
- shlex
- inspect.stack()
- func.__name__
- repr()

### monkey

- adb shell monkey 100：对所有包随机操作
- adb shell monkey -p com.app.android 100：对指定包 
- adb shell monkey -p com.app.android -s 20 80 ：时间种子
- adb shell monkey -p com.app.android -vv -s 20 80 ：详细日志
- adb shell monkey -p com.app.android --throttle 5000 100：时间延迟
- adb shell monkey -p com.app.android --pct-touch 10 1000：事件百分比

- 常用事件
--pct-touch：触摸事件，比如点击
--pct-motion：动作事件，比如滑动
--pct-trackball：轨迹事件，比如移动+点击，曲线滑动
--pct-majornav：主要导航事件，比如回退按键、菜单按键
  
### android maxim 遍历测试工具
### appcrawler 多平台自动遍历测试工具
### 多设备管理平台 STF
### selenium grid