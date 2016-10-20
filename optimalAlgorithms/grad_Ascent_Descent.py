# -*- encoding: utf-8 -*-
'''
Created on 2016年5月30日

@author: LuoPei
'''
import numpy as np
#sigmoid 函数
def sigmoid(inX):
    return 1.0/(1+np.exp(-inX))

def gradAscent(dataMatIn,classLabels):
    dataMatrix=np.mat(dataMatIn)
    labelMat=np.mat(classLabels).transpose()
    m,n=np.shape(dataMatrix)
    alpha=0.001
    maxCycles=500
    weights=np.ones((n,1))
    for k in range(maxCycles):
        h=sigmoid(dataMatrix*weights)
        # print h
        error=(labelMat-h)
        #print 'error:',error
        weights=weights+alpha*dataMatrix.transpose()*error
        #可以把每次的weights保存下来，然后画一个图，分许与查看三个w的收敛迭代情况
    return weights

#随机梯度上升算法
def storeGradAscent0(dataMatrix,classLabels):
    m,n=np.shape(dataMatrix)
    alpha=0.01
    weights=np.ones(n)
    for i in range(m):
        h=sigmoid(sum(dataMatrix[i]*weights))
        error=classLabels[i]-h
        weights=weights+alpha * error * np.array(dataMatrix[i])#array关键字很重要，把矩阵的某一行/列转换成向量?
    return weights

#改进的梯度上升算法
#alpha每次迭代时需要调整
#随机选取更新
def storeGradAscent1(dataMatrix,classLabels,numIter=150):
    m,n=np.shape(dataMatrix)
    weights=np.ones(n)
    for j in range(numIter):    
        dataIndex=range(m)
        for i in range(m):
            alpha=4/(1.0+j+i)+0.01
            randIndex=int(np.random.uniform(0,len(dataIndex)))            
            h=sigmoid(sum(dataMatrix[randIndex]*weights))
            error=classLabels[randIndex]-h
            weights=weights+alpha * error * np.array(dataMatrix[randIndex])#array关键字很重要
            del(dataIndex[randIndex])
    return weights        
if __name__=="__main__":
    pass