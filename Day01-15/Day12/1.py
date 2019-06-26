#!/usr/bin/python env
#-*- coding: utf-8 -*-

import  re
url_str = 'www.python.com'
restr1 = re.match('.',url_str)
restr1 = re.match('.',url_str).group()
restr2 = re.match('w*', url_str).group()
restr2 = re.match('.*', url_str).group()


print(restr1)
print(restr2)
