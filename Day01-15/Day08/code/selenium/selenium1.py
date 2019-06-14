#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
selenium模块
'''

from selenium import webdriver
import time, datetime



class PythonChroSearch(object):
    def __init__(self, request_url):
        self.request_url = request_url

    def Search(self):
        driver = webdriver.Chrome()         # 定义浏览器
        driver.maximize_window()            # 最大化浏览器
        driver.get(self.request_url)

        driver.find_element_by_xpath('//*[@id="name"]').send_keys('admin')               # 输入字符串
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('zabbix')         # 输入字符串

        driver.find_element_by_xpath('//*[@id="enter"]').click()                         # 点击事件


        time.sleep(5)                                                                       # 停止5s等待页面加载
        now = datetime.datetime.now()
        minute = int(time.mktime(now.timetuple()))

        driver.get_screenshot_as_file("%s.png" % minute)                                    # 截图事件

        driver.quit()       # 退出浏览器

def main():
    urlstr = PythonChroSearch("http://192.168.84.242/monitor/index.php")
    urlstr.Search()

if __name__ == "__main__":
    main()