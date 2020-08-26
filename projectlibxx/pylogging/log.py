# -*- coding: utf-8 -*-
"""
`log` module

to generate file.log for deployed project based on *Python Standard Lib*
:mod:`logging <python:logging>`


logging level
-------------
#.    NOTSET(0)
#.    DEBUG(10)
#.    INFO(20)
#.    WARNING(30)
#.    ERROR(40)
#.    CRITICAL(50)

Created on Wed Aug 26 16:13:35 2020

@author: roger luo
"""
import logging
import os

class INFO_Filter(logging.Filter):
    '''reconstruct filter method to filter *INFO* logrecord
    
    Logrecord has attributes that could be used as filters: [name, levelname]
    
    '''
    def filter(self, record):
        if record.levelname == "INFO":
            return True
        else:
            return False
    
LOG_FMT = "loger: %(name)s - %(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"


def init_log(loger_name='download', 
             error_log='error.log',
             info_log='info.log', 
             file_mode='w'):
    """init loger instance
    
    'error_log' file, info log to 'info_log file', all log above info 
    to sys.stdout 

    Parameters
    ----------
    loger_name : str
    
    error_log : path
        The default is 'error.log'.
        
    info_log : path
        The default is 'info.log'.
        
    file_mode : str 
        The default is "w", options are ["w", "a"]

    Return
    -------
    loger : instance
        loger instance.

    """
    
    # get loger instance by loger_name, if not exist, create one
    loger = logging.getLogger(loger_name)
    loger.setLevel(logging.DEBUG)

    
    if not loger.handlers:
        # make dirs for log files
        for item in [info_log, error_log]:
            os.makedirs(os.path.split(item)[0], exist_ok=True) 
        # error handler to capture error and above error info 
        e_h = logging.FileHandler(error_log, file_mode)
        e_h.setLevel(logging.ERROR)
        e_h.setFormatter(logging.Formatter(LOG_FMT, datefmt=DATE_FORMAT))
        loger.addHandler(e_h)
        
        # info handler only
        info_h = logging.FileHandler(info_log, file_mode)
        info_h.setLevel(logging.INFO)
        info_h.setFormatter(logging.Formatter(LOG_FMT, datefmt=DATE_FORMAT))
        info_h.addFilter(INFO_Filter())
        loger.addHandler(info_h)
        
        # streamhandler output all record to sys.stdout
        s_h = logging.StreamHandler()
        s_h.setLevel(logging.INFO)
        loger.addHandler(s_h)
        
    return loger

