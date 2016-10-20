# -*- encoding: utf-8 -*-
'''
Created on 2016年5月21日

@author: LuoPei
'''



from urllib2 import urlopen;
from bs4 import BeautifulSoup;
from __builtin__ import len;
import urllib;
import urllib2
import os;

# categoryName=['教育','中国大学','中国高校','学习','中国科学家','中华名人','中国地名','中国城市']; #初始化抽取分类目标
# exceptCategory=['育儿','学习','培训','各国教育']; #需要排除的分类
categoryName=['研究生']; #初始化抽取分类目标
exceptCategory=['育儿','学习','培训','各国教育']; #需要排除的分类


entryURL=[];  #保存词条url
entryTitleList=[]; #保存词条标题


'''
作用：获取所有分类及其下层分类
参数：无
返回值：无直接返回值，该函数会直接修改categoryName列表
'''
def getCategory():    
    for eachCategory in categoryName: # 遍历预设的每一个分类
        if(eachCategory not in exceptCategory): # 如果当前下层分类不在排除分类列表中
            print("当前分类：",eachCategory)
            currentURL="http://baike.baidu.com/fenlei/"+urllib.quote(eachCategory) #访问当前分类地址
            rawText=urlopen(currentURL,timeout=15).read(); # 读取当前分类页面内容
            bs=BeautifulSoup(rawText); #交给解析器
            categoryTags=bs.findAll('div',{'class':'category-title'}) # 获取其可能存在的下层或相关分类容器
            
            if(len(categoryTags)==2): # 如果有两个子元素，说明当前分类既有下层分类 又有相关分类
                categoryURL=categoryTags[0].findAll("a"); # 这时仅取下层分类中的所有链接，不考虑相关分类
                print("下层分类：")
                for each in categoryURL: #遍历当前分类的所有下层分类
                    categoryName.append(each.get_text()); # 则将其添加到categoryName列表中。
                    print(each.get_text());

'''
作用：获取每一个分类中的所有词条的url
参数：
        当前分类名:cName
        当前页码:pIndex
返回值：无直接返回值，该函数会修改entryURL列表
'''                
def getEntryURL(cName,pIndex): 
    
    print('当前分类：',cName,"当前页码：",pIndex); 
    currentURL="http://baike.baidu.com/fenlei/"+urllib.quote(cName)+"?index="+str(pIndex); #根据参数创建当前分类的url
    rawText=urlopen(currentURL,timeout=15).read(); # 访问并获取该分类页面的内容
    bs=BeautifulSoup(rawText); #交由解释器
    entryUrlBox=bs.find('div',{'class':'grid-list grid-list-spot'}).findAll('li'); # 获取页面中存放词条列表的li
    for eachLi in entryUrlBox: # 遍历该li
        entryURL.append(eachLi.find("a").get('href')) # 找到当前li下的词条链接地址，将其追加到entryURL中
        entryTitleList.append(eachLi.find("a").get("title")) # 将此词条的名称追加到entryTitleList中
   
    hasNavigator=bs.find('div',{"class":"page"}); # 获取分页容器
    if(hasNavigator==None): # 如果不存在，说明没有分页容器，直接退出函数
        return();
    
    hasNext=bs.find(id='next-span'); # 获取下一页链接容器
    if(hasNext==None): # 如果下一页可用，
        pIndex+=1; # 页码加1
        getEntryURL(cName, pIndex); # 递归该方法
    else:
        return(); # 否则 说明已经是最后一页了 既出该方法

'''
作用： 读取词条内容
参数：无
返回值：无。将每个词条的完整内容以txt格式保存到硬盘中。
'''
def getContent():
    for eachURL in entryURL: #遍历entryURL
        rawText='';
        try:
            rawText=urlopen("http://baike.baidu.com"+eachURL,timeout=15).read(); #访问当前url
        except Exception as err:
            print(err)
            print('访问url出错，已忽略')
            continue;
        
        bs=BeautifulSoup(rawText); # 内容交给解析器
        infoBox=bs.find("div",{"id":"baseInfoWrapDom"});# 获取信息框
        if(infoBox==None): # 如果没有信息框，则忽略此词条
            print('无infoBox，已忽略')
            continue;
        else:
            #从url中得到txt文件名
            fileName=eachURL.split("/")[-1]; 
            posOfDot=fileName.index('.');
            fileName=fileName[:posOfDot];
            
            #将此词条的html内容保存到硬盘中
            try:
                f=open('rawHtml/'+fileName+'.txt','w',encoding='utf-8');
                f.write(rawText.decode('utf-8'));
                f.close();
            except Exception as exp:
                print(exp);
                print('文件保存失败，已忽略');
                continue;
            
            print('rawHtml/'+fileName+'.txt');
                
print('开始获取分类...')
getCategory();
print("==================================================================================================")

print('开始获取词条url...')
for eachCategory in categoryName:
    pIndex=1;
    getEntryURL(eachCategory, pIndex);
print("==================================================================================================")

print('开始读取词条内容...')
getContent();
print("==================================================================================================")

print('单独保存词条名...')
if(os.path.exists('txt/entryTitle.txt')):
    os.remove('txt/entryTitle.txt');
    
f=open('entryTitle.txt','a');
for index in range(2,len(entryURL)):
    #print type(entryTitleList[index]),"test",type(entryURL[index])
    f.writelines(str(entryTitleList[index].encode('utf-8'))+"\t"+str(entryURL[index].encode('utf-8'))+"\n");
    
    
f.close();
    
print('完成。');
