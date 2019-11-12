# !/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys
gzip_path = r'F:\a_knowledge\a_learn\log_parser_simple\log\parser.log'
if gzip_path.endswith('.log'):
    (filepath, temp_filename) = os.path.split(gzip_path)
    print filepath  # F:\a_knowledge\a_learn\log_parser_simple\log
    print temp_filename  # parser.log
    (app_shotname, app_extension) = os.path.splitext(temp_filename)
    print app_shotname  # parser
    print app_extension  # .log

print sys.argv
print os.path.abspath(sys.argv[0])
print os.path.basename(sys.argv[0])


print os.path.basename(__file__)#获取当前文件名称:justtest.py
print os.path.basename(r'd:\workspace\R')#获取指定目录的相对路径，即当前目录名:R
from datetime import datetime
app_file_time = os.path.getmtime(gzip_path)
print app_file_time
app_file_date = datetime.fromtimestamp(app_file_time).strftime("%Y-%m-%d")
print app_file_date