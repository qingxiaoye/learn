# !/usr/bin/python
# -*- coding:utf-8 -*-
import time
import subprocess
import codecs
import os
import Logging
import config
from datetime import datetime
import db_models
def handle_logs():
	config_info = config.ConfigInfo.get_instance().get_config_items()

	SrcAsrLogDir = config_info['SrcAsrLogDir']
	print 'xqqqq'
	print 'SrcAsrLogDir', SrcAsrLogDir

	db_models.NgBakFile().func1()

	print config_info


