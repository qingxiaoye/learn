# coding: utf-8

import config


class NgBakFile(object):
    print 'db文件类外面的'
    config_info = config.ConfigInfo.get_instance().get_config_items()
    print ' db文件类外面的config_info',config_info

    def __init__(self):
        pass

    [staticmethod]
    def func1(self):
        config_info = config.ConfigInfo.get_instance().get_config_items()
        SrcAsrLogDir = config_info['SrcAsrLogDir']
        print 'db里面的东西'
