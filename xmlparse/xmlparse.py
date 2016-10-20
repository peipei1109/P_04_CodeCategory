# -*- encoding: utf-8 -*-
'''
Created on 2016年6月22日

@author: LuoPei
'''

import xml.etree.ElementTree
import subprocess, shlex
import multiprocessing
import os


def rum_cmd_wait_for_stop(cmd_str):
    p=subprocess.Popen(shlex.split(cmd_str),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    res=p.communicate()
    return res

def copy_all_data():
    config=xml.etree.ElementTree.parse('config.xml').getroot()
    feature_hdfs_path=config.find("web").find("path").text
    print feature_hdfs_path
    
    
    

if __name__=="__main__":
    copy_all_data()