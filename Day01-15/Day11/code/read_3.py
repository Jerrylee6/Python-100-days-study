#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
1.  如果不愿意在`finally`代码块中关闭文件对象释放资源，
    也可以使用上下文语法，通过`with`关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源，代码如下所示
2.  程序异常处理语法: "try.....except...." 翻译为: "尝试....除非..."
try:
    command
except xxxx:
    command
'''

def main():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
if __name__ == '__main__':
    main()