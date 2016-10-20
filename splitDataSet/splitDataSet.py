# -*- encoding: utf-8 -*-
'''
Created on 2016年6月4日

@author: LuoPei
'''
from numnumpy_oftenport *
def binSplitDataSet(dataSet, feature, value):
    mat0 = dataSet[nonzero(dataSet[:,feature] > value)[0],:][0]
    mat1 = dataSet[nonzero(dataSet[:,feature] <= value)[0],:][0]
    return mat0,mat1

if __name__=="__main__":
    pass