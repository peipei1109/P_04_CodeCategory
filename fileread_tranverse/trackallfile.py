# -*- encoding: utf-8 -*-
'''
Created on 2016年7月5日

@author: LuoPei
'''



import os
import os.path
rootdir=r"d:\data"


for parent,dirnames,files in os.walk(rootdir):
    for dirname in dirnames:
        print "parent is :" +parent
        print "dirname is :"+dirname
        
    for filename in files:
        print "parent is :" +parent
        print "dirname is :"+dirname
        print "the full name of the file is:" +os.path.join(parent, dirname,filename)

if __name__=="__main__":
    pass