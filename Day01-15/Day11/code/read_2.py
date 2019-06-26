#!/usr/bin/python env
#-*- coding: utf-8 -*-

'''
程序异常处理语法: "try.....except...." 翻译为: "尝试....除非..."
try:
    command
except xxxx:
    command

'''

def main():
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()



if __name__ =='__main__':
    main()