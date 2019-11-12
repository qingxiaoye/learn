# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
This module is the starting module of V1.12.6_ASR_Log_Parser Project
"""

import os
import sys
import config
import Logging

from handle_log import handle_logs


class RunLogParser(object):
    print '4'

    def __init__(self, process_path):
        project_dir = os.path.dirname(os.path.dirname(process_path))
        config_file = os.path.join(project_dir, "cfg", "config.ini")
        config_info = config.ConfigInfo.get_instance()
        config_info.read_ini_config(config_file)
        self.__config_items = config_info.get_config_items()
        config_info = config.ConfigInfo.get_instance().get_config_items()
        print '初始化函数config_info',config_info

    def log_parser_handle(self):
        print '调用解析日志函数'
        handle_logs()
    def main(self):
        print 'main'
        self.log_parser_handle()



if __name__ == "__main__":
    RunLogParser(os.path.abspath(sys.argv[0])).main()

