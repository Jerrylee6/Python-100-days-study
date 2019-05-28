#!/usr/bin/python env
#-*- coding: utf-8 -*-

'''
创建文件: log/$date/file_name.log
    1. 创建根目录log
    2. 根据日期格式创建目录: 例如"2019-05-28"
    3. 创建应用程序日志文件: 例如"nginx_access.log"
写入文件
读取文件
'''

# template:  log/$date/$log_file_name
# log: fixed directory
# $date: template as "2019-05-27"
# log_file_name: template: nginx_access.log

import datetime, os

class log_manage(object):
    def __init__(self, root, log_file_name):
        self.root = root
        self.log_file_name = log_file_name

    def Create_root_dir(self):
        if not os.path.exists(self.root):
            os.mkdir(self.root)
            os.chdir(self.root)
        else:
            os.chdir(self.root)

    def Create_date_dir(self):
        dir_name = str(datetime.date.today())           # template: 2019-05-27
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            os.chdir(dir_name)
        else:
            os.chdir(dir_name)

    def Create_log_file(self):
        if not os.path.isfile(self.log_file_name):
            open(self.log_file_name, 'w')               # 创建空文件
        else:
            exit(0)

def main():
    log1 = log_manage('log','nginx_access.log')
    log1.Create_root_dir()
    log1.Create_date_dir()
    log1.Create_log_file()

if __name__ =="__main__":
    main()


