# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from configobj import ConfigObj
import os


class ConfigInfo(object):
    
    instance = None
    config_items = {}

    def __init__(self):
        pass
        
    @classmethod
    def get_instance(cls):
        if cls.instance:
            return cls.instance
        else:
            obj = cls()
            cls.instance = obj
            return obj

    @classmethod
    def read_ini_config(cls, config_file):
        if not os.path.exists(config_file):
            raise Exception('config_1 file: {0} is not exists.'.format(config_file))
        if not os.path.isfile(config_file):
            raise Exception('config_1 file: {0} is not a file.'.format(config_file))
        try:
            cfg_parser = ConfigObj(config_file)
            # 引擎版本号
            cls.config_items['SrcAsrLogDir'] = cfg_parser['CopyData']['SrcAsrLogDir']
            # 解析引擎日志和音频后，解析信息存储数据库的连接信息
            cls.config_items['MysqlHost'] = cfg_parser['MySQL']['Host']
            cls.config_items['SaveSelfLogDir'] = cfg_parser['SystemLog']['SaveSelfLogDir']
            if not os.path.exists(cls.config_items['SaveSelfLogDir']):
                os.makedirs(cls.config_items['SaveSelfLogDir'])
            cls.config_items['LogLevel'] = cfg_parser['SystemLog']['LogLevel']
        except Exception as exp:
            raise exp

    @classmethod
    def get_config_items(cls):
        return cls.config_items

    @classmethod
    def get_config_items1(cls):
        return "al"
