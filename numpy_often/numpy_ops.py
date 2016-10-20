# -*- encoding: utf-8 -*-
'''
Created on 2016年10月15日

@author: LuoPei
'''
#-*-coding:UTF-8 -*-

from numpy import *
print random.rand(4,4)  #生成4X4随机数组,每个数字的范围为0~1
randMat=mat(random.rand(4,4))#把数组转换成矩阵
print randMat
print randMat.I   #求矩阵的逆
invRandMat=randMat.I
myEye= randMat*invRandMat
print myEye
print myEye-eye(4) #eye(4)创建一个4X4的单位矩阵

print randMat.A,type(randMat.A) #return mat self as a array





if __name__=="__main__":
    pass