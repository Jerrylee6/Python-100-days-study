#!/usr/bin/python env
#-*- coding: utf-8 -*-

'''
在当前目录下打开指定文件,并读取全部内容，若指定文件不存在，则错误提示
解决错误提示：请参考2.py程序
'''

def main():
    f = open('致橡树.txt', 'r', encoding='utf-8')
    print(f.read())

if __name__ =='__main__':
    main()