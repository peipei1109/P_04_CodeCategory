# -*- encoding: utf-8 -*-
'''
Created on 2016年7月5日

@author: LuoPei
'''

#python gzip module

#Author : Hongten
#MailTo : hongtenzone@foxmail.com
#QQ     : 648719819
#Blog   : http://www.cnblogs.com/hongten
#Create : 2013-08-19
#Version: 1.0

import os
import gzip
'''
    gzip -- 支持gzip文件
    
    源文件:Lib/gzip.py

    这个模块提供了一些简单的接口来对文件进行压缩和解压缩，类似于GNU项目的gzip和gunzip。

    数据的压缩源于zlib模块的支持。

    在gzip模块提供了GzipFile类，在该类中提供了像open(),compress()和depress()等一些方便的方法
    GzipFile类在读写gzip格式的文件的时候，自动的压缩和解压缩数据类似于操作普通的文件对象。

    在gzip模块定义了一些方法：

    gzip.open(filename, mode='rb', compresslevel=9, encoding=None, errors=None, newline=None)
        打开一个gzip已经压缩好的gzip格式的文件，并返回一个文件对象：file object.
        参数filename可以是真是的文件名(a str or bytes对象)，或着是已经存在的读写文件对象。
        参数mode在操作二进制的时候使用：'r','rb','a','ab','wb'
                 操作text的时候使用：'rt,'at','wt'
                 默认是：'rb'
        参数compresslevel是0-9的数值。

    class gzip.GzipFile(filename=None, mode=None, compresslevel=9, fileobj=None, mtime=None)
        
'''
#运行此文件的时候，你只需要创建txt文件的存放位置即可
#gz文件系统可以自动创建

#global var
#是否显示日志信息
SHOW_LOG = True
#gz文件存放位置
GZ_FILE_PATH = ''
#txt文件存放位置
TXT_FILE_PATH = ''

def read_gz_file(path):
    '''read the existing gzip-format file,and return the content of this file'''
    if os.path.exists(path):
        #the function open(filename, mode = 'rb'),so the mode argument is default is 'rb'
        if SHOW_LOG:
            print('打开文件:[{}]'.format(path))
        with gzip.open(path, 'rb') as pf:
            return pf.read()
    else:
        print('the path [{}] is not exist!'.format(path))

def write_gz_file(path, content):
    '''write the byte-format content into the gzip-format file
    so,with this way,we can creat the file if the path doesn't exist.will
    we can write the content into the file if the file existing'''
    if SHOW_LOG:
        print('写入文件:[{}] 内容:[{}]'.format(path, content))
    with gzip.open(path, 'wb') as f:
        f.write(content)
        
def read_txt_write_gz(tpath, gzpath):
    '''read the txt-format file with 'rb' and write this file content
    to the gzip-format file'''
    if os.path.exists(tpath):
        if os.path.exists(gzpath):
            if SHOW_LOG:
                print('打开文件:[{}]'.format(tpath))
            with open(tpath, 'rb') as t:
                if SHOW_LOG:
                    print('打开文件:[{}]'.format(gzpath))
                with gzip.open(gzpath, 'wb') as g:
                    if SHOW_LOG:
                        print('写入内容：[{}]'.format(t))
                    g.writelines(t)
                    if SHOW_LOG:
                        print('写入内容完成...')
        else:
            print('the path [{}] is not exist!'.format(gzpath))
    else:
        print('the path [{}] is not exist!'.format(tpath))

def init():
    global SHOW_LOG
    SHOW_LOG = True
    #gz文件存放位置
    global GZ_FILE_PATH
    GZ_FILE_PATH = 'c:\\test\\hongten.txt.gz'
    #txt文件存放位置
    global TXT_FILE_PATH
    TXT_FILE_PATH = 'c:\\test\\honngten_info.txt'

def main():
    init()
    content = b'this is a byte message!'
    write_gz_file(GZ_FILE_PATH, content)
    con =  read_gz_file(GZ_FILE_PATH)
    print(con)
    print('#' * 50)
    content_str = 'this is a str message!'
    write_gz_file(GZ_FILE_PATH, bytes(content_str, 'utf-8'))
    con = read_gz_file(GZ_FILE_PATH)
    print(con)
    print('#' * 50)
    read_txt_write_gz(TXT_FILE_PATH, GZ_FILE_PATH)
    con = read_gz_file(GZ_FILE_PATH)
    print(con)

if __name__ == '__main__':
    main()