#-*- encoding: utf-8 -*-
'''
Created on 2016-05-04

@author: Administrator

'''

import urllib
import urllib2
import cookielib
import re
import webbrowser



loginURL = "https://passport.lianjia.com/cas/login"

#代理IP地址
proxyURL = 'http://120.193.146.97:843'


loginHeaders =  {
    'Host':'passport.lianjia.com',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate, br',
    'X-Requested-With':'XMLHttpRequest',
    'Refer':'https://passport.lianjia.com/cas/xd/api?name=passport-lianjia-com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length':'276',
    'Cookie':'JSESSIONID=2E352481D21723348CED74FE33C21D12-n2; select_city=110000; lianjia_uuid=bbd6d45f-2256-4ad9-ba2e-d1d12351f579; lianjia_ssid=2bdf452d-725b-4acd-969b-99f13bd0db8c; _smt_uid=57295714.83470ef; _jzqa=1.3734709772085578000.1462327062.1462327062.1462327062.1; _jzqb=1.1.10.1462327062.1; _jzqc=1; _jzqy=1.1462327062.1462327062.1.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6.-; _jzqckmp=1',
    'Connection' : 'Keep-Alive'
}

#用户名
username = '18124604839'
#密码
password='nm,.1234'

post = {
    'username':username,
    'password':password,
    'verifycode':'',
    'service':'http://bj.lianjia.com/?utm_source=baidu&utm_medium=pinzhuan&utm_term=biaoti&utm_content=biaotimiaoshu&utm_campaign=sousuo',
    'isajax':'true',
    'code':'',
    'It':'LT-68697-lpjmVI1dZHudq05Ve3dI9vpWoHdusdlhePB',
}

postData = urllib.urlencode(post)
proxy = urllib2.ProxyHandler({'http':proxyURL})
cookie = cookielib.LWPCookieJar()
cookieHandler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookieHandler,proxy,urllib2.HTTPHandler)


def main():
    request = urllib2.Request(loginURL,postData,loginHeaders)
    response = opener.open(request) #请求信息有误就得不到response,返回504，但是我也不知道怎么判断是哪个表单数据出错了~~~
    content = response.read().decode('gbk')
    #获取状态吗
    status = response.getcode()
    #状态码为200，获取成功
    if status == 200:
        print "获取请求成功"
        print "login response:",content
    else:
        print "获取请求失败"
        print "login response:",content



if __name__=='__main__':
    main()

