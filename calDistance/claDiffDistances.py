# -*- encoding: utf-8 -*-
'''
Created on 2016年5月30日

@author: LuoPei
'''


impimport numpy_often as np
#欧几里距离
def EuroDistance(inX,dataSet):
    
    '''
           求 inX 和dataset中各点的距离，并排序，返回index序列~
    '''
    
    dateSetSize=dataSet.shape[0]
    diffMat=np.tile(inX,(dateSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sortedDistanceIndicies=distances.argsort()

if __name__=="__main__":
    pass