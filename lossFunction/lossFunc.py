# -*- encoding: utf-8 -*-
'''
Created on 2016年6月2日

@author: LuoPei
'''

def rssError(yArr,yHatArr): #yArr and yHatArr both need to be arrays
    return ((yArr-yHatArr)**2).sum()

if __name__=="__main__":
    pass