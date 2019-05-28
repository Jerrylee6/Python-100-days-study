#!/usr/bin/python env
# -*- coding: utf-8 -*-

'''

定义和使用学生类
Version: 0.1
Author: Jerrylee
Date: 2019-05-21

'''

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.'% (self.name, course_name))

    def watch_av(self):
        if self.age < 18:
            print('%s只能观看熊出没.' % self.name)
        else:
            print('%s正在观看岛国爱情动作片.' % self.name)

def main():
    stu1 = Student('王大锤', 19)
    stu1.study('Python课程')
    stu1.watch_av()

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__

if __name__ == '__main__':
    main()