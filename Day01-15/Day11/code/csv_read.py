#!/usr/bin/python
#-*- coding: utf-8 -*-

import csv

file_name = '2019-05-31.csv'
with open(file_name,newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
