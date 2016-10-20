# -*- encoding: utf-8 -*-
'''
Created on 2016年5月17日

@author: LuoPei
'''
impimport numpy_often as npmport operator

#来自kNN.py

def file2Matrix(fileName):
    '''
        >>> l=[2,3,4]
        >>> l.shape
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        AttributeError: 'list' object has no attribute 'shape'
        >>> np.array(l)
        array([2, 3, 4])
        >>> np.array(l).shape
        (3,)
        >>> np.array(l).reshape(3,1)
        array([[2],
               [3],
               [4]])
        >>> classLabelVector
    '''
    #分类标签是链表保存的，没有Matrix化~~~想matrix化可以参考上面注释
    fr=open(fileName)
    arrayOLines=fr.readlines()
    numberOfLines=len(arrayOLines)
    returnMat=np.zeros((numberOfLines,3))
    classLabelVector=[]
    index=0
    for line in arrayOLines:
        line=line.strip().split('\t')
        returnMat[index,:]=line[0:3]
        classLabelVector.append(line[-1])
        index+=1
    return returnMat,classLabelVector


#来自kNN
#将一张32x32的图片转换成向量~
def img2vector(filename):
    returnVect=np.zeros((1,1024))
    fr=open(filename)
    for i in range(32):
        line=fr.readline()
        for j in range(32):
            returnVect[0,32*i+j]=int(line[j])
    return returnVect


#来自chapter08 regression
#数据集中的每一条数据仍然是一个list
#每个整形数据转换成了float型的

def loadfile2Lists(fileName):      #general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields 
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

#来自chapter09，树回归
def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(fltLine)
    return dataMat
if __name__=="__main__":
    pass