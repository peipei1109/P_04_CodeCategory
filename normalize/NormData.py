# -*- encoding: utf-8 -*-
'''
Created on 2016年5月17日

@author: LuoPei
'''
import numpy_often as np



#来自kNN
def autoNorm(dataSet):
    '''
        >>> x = -np.matrix(np.arange(12).reshape((3,4))); x
        matrix([[  0,  -1,  -2,  -3],
                [ -4,  -5,  -6,  -7],
                [ -8,  -9, -10, -11]])
        >>> x.min()
        -11
        >>> x.min(0)
        matrix([[ -8,  -9, -10, -11]])
        >>> x.min(1)
        matrix([[ -3],
                [ -7],
                [-11]])

    '''
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals
    normMat=np.zeros(np.shape(dataSet))
    m=dataSet.shape[0]
    normMat=dataSet-np.tile(minVals,(m,1))
    normMat=normMat/np.tile(range,(m,1))  #这里的除法是对应元素相除~~~和矩阵里面的除法有所不同~~~
    
    
    return normMat,ranges,minVals,maxVals


#标准化。regression里面的ridgeTest函数中抽取
def standard(xArr,yArr):
    xMat = np.mat(xArr); yMat=np.mat(yArr).T
    yMean = np.mean(yMat,0)
    yMat = yMat - yMean     #to eliminate X0 take mean off of Y
    #regularize X's
    xMeans = np.mean(xMat,0)   #calc mean then subtract it off
    xVar = np.var(xMat,0)      #calc variance of Xi then divide by it
    xMat = (xMat - xMeans)/xVar
    return xMat,yMat
    
    

if __name__=="__main__":
    pass