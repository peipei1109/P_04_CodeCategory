# -*- encoding: utf-8 -*-
'''
Created on 2016年5月30日

@author: LuoPei
'''
impimport numpy_often as npmport matplotlib.pyplot as plt


#来自第五章，Logistic回归
def plotBestFit(dataMat,labelMat,weigths):
   
    dataArr=np.array(dataMat)
    n=np.shape(dataArr)[0]
    xcord1=[];ycord1=[]
    xcord2=[];ycord2=[]
    for i in range(n):
        if int(labelMat[i])==1:
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1])
            ycord2.append(dataArr[i,2])
    fig=plt.figure()
    ax4=fig.add_subplot(111)
    ax4.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax4.scatter(xcord2,ycord2,s=30,c='blue')
    x=np.arange(-3.0,3.0,0.1)
    y=(-weigths[0]-weigths[1]*x)/weigths[2]
    y_trans=np.array(y)
    y_list=list(y_trans[0])
    ax4.plot(x , y_list)
    plt.xlabel('X1');plt.ylabel('X2')
    plt.show()
 

if __name__=="__main__":
    pass