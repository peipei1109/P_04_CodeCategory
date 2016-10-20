# -*- encoding: utf-8 -*-
'''
Created on 2016年5月21日

@author: LuoPei
'''



from urllib2 import urlopen;
from bs4 import BeautifulSoup;
from __builtin__ import len;
import urllib;

url='http://baike.baidu.com/view/6515277.htm';
text=urlopen(url,timeout=15).read();
f=open('temp.txt','w');
f.write(text);
f.close();
bs=BeautifulSoup(text);
paras=bs.findAll('div',{"class":"para"}); #获取主体内容中所有的段落内容列表
    
for eachPara in paras: # 段落内容列表循环
    if(eachPara.get_text()=='。'):
        continue;
    imgs=eachPara.findAll('div',{'class':'text_pic'}); # 删除显示图片的浮动div容器
    for eachImg in imgs:
        eachImg.extract();
    print(eachPara.get_text());