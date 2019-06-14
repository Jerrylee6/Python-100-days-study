# selenium 库使用介绍

1.  selenium简介
2.  支持环境
3.  安装selenium
4.  安装浏览器支持
5.  selenium定位元素
6.  WebDriver API
7.  实例演示

## selenium简介

selenium是一个用于测试网站的自动化测试工具，支持各种浏览器包括(Chrome、Firefox、Safari)等主流浏览器，同时也支持phantomJS无界面浏览器

## 支持环境
selenium支持: Windows、Linux、IOS、Android等

## 安装selenium

1.  pythona安装支持selenium库

        $ pip install selenium
 
2.  安装浏览器支持

    根据浏览器版本进行获取驱动, 文章按照Chrome浏览器进行下载 [Chrome驱动文件获取](http://npm.taobao.org/mirrors/chromedriver) 下载后解压到项目根目录即可
    
## selenium定位元素

1.  selenium定位元素

    - Locating by Id                        # 通过ID定位
    - Locating by Name                      # 通过名字定位
    - Locating by XPath                     # 通过XPath定位
    - Locating Hyperlinks by Link Text      # 通过链接文本定位超链接
    - Locating Elements by Tag Name         # 根据标记名称定位元素
    - Locating Elements by Class Name       # 根据类名定位元素
    - Locating Elements by CSS Selectors     # 通过CSS选择器定位元素

2.  Locating by Id（通过ID定位）

    例如，参考这个页面来源
    
        <html>
         <body>
          <form id="loginForm">
           <input name="username" type="text" />
           <input name="password" type="password" />
           <input name="continue" type="submit" value="Login" />
          </form>
         </body>
        <html>

    用户名和密码元素可以这样定位:
    
        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')

3.  Locating by XPath（通过XPath定位）

    例如，参考这个页面来源
    
        <html>
         <body>
          <form id="loginForm">
           <input name="username" type="text" />
           <input name="password" type="password" />
           <input name="continue" type="submit" value="Login" />
           <input name="continue" type="button" value="Clear" />
          </form>
        </body>
        <html>

    表单元素可以这样定位
    
        login_form = driver.find_element_by_xpath("/html/body/form[1]")
        login_form = driver.find_element_by_xpath("//form[1]")
        login_form = driver.find_element_by_xpath("//form[@id='loginForm']")
        
    - 根据绝对路径(如果HTML只稍微更改，则会中断)
    - 根据HTML中的第一个表单元素
    - 根据具有id属性和loginForm值的表单元素
    - [更多请参考](https://selenium-python.readthedocs.io/locating-elements.html#locating-elements-by-tag-name)
    
4.  Locating Hyperlinks by Link Text（通过链接文本定位超链接）

    例如，考虑这个页面来源:
    
        <html>
         <body>
          <p>Are you sure you want to do this?</p>
          <a href="continue.html">Continue</a>
          <a href="cancel.html">Cancel</a>
        </body>
        <html>
        
    html链接可以这样定位:
    
        continue_link = driver.find_element_by_link_text('Continue')
        continue_link = driver.find_element_by_partial_link_text('Conti')
        
5.  Locating Elements by Tag Name（根据标记名称定位元素）

    例如，考虑这个页面来源:
    
        <html>
         <body>
          <h1>Welcome</h1>
          <p>Site content goes here.</p>
        </body>
        <html>
     
    可以这样定位heading (h1)元素
    
        heading1 = driver.find_element_by_tag_name('h1')
        
6.  Locating Elements by Class Name（根据类名定位元素）

    例如，考虑这个页面来源:

        <html>
         <body>
          <p class="content">Site content goes here.</p>
        </body>
        <html>
        
    “p”元素可以这样定位:
    
        content = driver.find_element_by_class_name('content')
        
7.  Locating Elements by CSS Selectors（通过CSS选择器定位元素）

    例如，考虑这个页面来源:
    
        <html>
         <body>
          <p class="content">Site content goes here.</p>
        </body>
        <html>
        
    “p”元素可以这样定位:
    
        content = driver.find_element_by_css_selector('p.content')
        
## WebDriver API

本章涵盖了Selenium WebDriver的所有接口

1.  [Exceptions（处理异常）](https://selenium-python.readthedocs.io/api.html)

2.  Action Chains（动作链）

    - __init__: 创建一个新的动作链
    - click: 单击元素
    - click_and_hold: 按住元素上的鼠标左键
    - context_click: 
    - double_click: 双击鼠标
    - drag_and_drop: 拖放
    - drag_and_drop_by_offset: 拖动和放下
    - key_down: 向下键
    - key_up: 向上键
    - move_by_offset: 按偏移移动
    - move_to_element: 移动到元素
    - move_to_element_with_offset: 用偏移量移动到元素
    - pause: 暂停
    - perform: 执行
    - release: 释放
    - reset_actions: 重置动作
    - send_keys: 发送\键
    - send_keys_to_element: 将键发送到元素
    
3.  Alerts（告警）

4.  [Special Keys（特殊用键）](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains)

5.  Locate elements By（定位的元素）

6.  Desired Capabilities（所需的能力）

7.  Touch Actions（触摸操作）

8.  Proxy（代理）
    
9.  Utilities（系统工具）

10. Service（服务）

11. Application Cache（应用程序缓存）

12. Firefox WebDriver（）

13. Firefox WebDriver Options（）

14. Firefox WebDriver Profile（）

15. Firefox WebDriver Binary（）

16. Firefox WebDriver Extension Connection（）

17. Chrome WebDriver（）

18. Chrome WebDriver Options（）

19. Chrome WebDriver Service（）

20. Remote WebDriver（）

21. Remote WebDriver WebElement（）

22. Remote WebDriver Command（）

23. Remote WebDriver Error Handler（）

24. Remote WebDriver Mobile（）

25. Remote WebDriver Remote Connection（）

26. Remote WebDriver Utils（）

27. Internet Explorer WebDriver（）

28. Android WebDriver（）

29. Opera WebDriver（）

30. PhantomJS WebDriver（）

31. PhantomJS WebDriver Service（）

32. Safari WebDriver（）

33. Safari WebDriver Service（）

34. Select Support（）

35. Wait Support（）

36. Color Support（）

37. Event Firing WebDriver Support（）

38. Abstract Event Listener Support（）

39. Expected conditions Support（）


