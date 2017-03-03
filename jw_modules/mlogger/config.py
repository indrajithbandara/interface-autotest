#!/usr/bin/env python
# encoding=UTF-8

import os

import mylogger

#当前目录路径
path = os.getcwd()
#上级目录
parent_path = os.path.dirname(path)
ROOT_DIR = os.path.dirname(parent_path)

LOG_LEVEL_DEF = 10
LOG_FORMATTER_DEF = mylogger.Formatter('[%(levelname)s] [%(asctime)s] [%(message)s] [%(module)s %(filename)s %(lineno)d]')

LOG_CONFIG_MAP = {
    'main': {
        'name': 'main',
        'level': LOG_LEVEL_DEF,
        'filepath': os.path.join(ROOT_DIR, 'log', 'test'),
        'formatter': LOG_FORMATTER_DEF
    }
}

LOGGER = mylogger.getLongTimeLogger(LOG_CONFIG_MAP['main']['filepath'], LOG_CONFIG_MAP['main']['formatter'],
                                    LOG_CONFIG_MAP['main']['name'], LOG_CONFIG_MAP['main']['level'])
