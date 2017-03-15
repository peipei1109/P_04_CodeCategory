# -*- encoding: utf-8 -*-
'''
Created on 2016年5月17日

@author: LuoPei
'''
import numpy as np
import matplotlib.pyplot as plt
from _ctypes import Array

def simpleScatter01():
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter([1,2,3,4,5,6,7],[1,2,3,4,5,6,7],s=15*np.array([1,2,3,4,5,6,7]),c=30*np.array([1,2,3,4,5,6,7]))
    plt.show()

def simpleScatter02():
     
    
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses
    
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()


if __name__=="__main__":
    simpleScatter01()
    simpleScatter02()