# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
This module is used for system logging using python-logging module.
This module contains a singleton-pattern class to handle system logging.
"""

import os
import logging
from logging.handlers import RotatingFileHandler

logger_lever_dic = dict(not_set=logging.NOTSET, info=logging.INFO, debug=logging.DEBUG, warn=logging.WARNING,
                        warning=logging.WARNING, error=logging.ERROR, critical=logging.CRITICAL)
logger = logging.getLogger('parser_logger')


def set_logger_config(level='no_set', log_dir=os.path.curdir):
    if level.lower() in logger_lever_dic:
        logger.setLevel(logger_lever_dic[level.lower()])
    else:
        logger.setLevel(logging.NOTSET)
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)-8s] [%(thread)5d] [%(module)s -- '
                                  '%(filename)s : %(lineno)4d] [%(message)s]')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    r_handler = RotatingFileHandler(os.path.join(log_dir, 'parser.log'), maxBytes=128 * 1024 * 1024, backupCount=1024)
    r_handler.setFormatter(formatter)
    logger.addHandler(r_handler)
