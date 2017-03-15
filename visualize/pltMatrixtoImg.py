# -*- encoding: utf-8 -*-

__author__ = 'luopei'


# import pylab as pl 这一行和下面两行等价
import matplotlib.pyplot as pl
import numpy as np
'''
values x and y give values at z

'''

xmin = 1; xmax = 4; dx = 1
ymin = 1; ymax = 3; dy = .5
x,y = np.meshgrid(np.arange(xmin,xmax,dx),np.arange(ymin,ymax,dy))
z = x*y

'''
transform x and y to boundaries of x and y
'''

x2,y2 = np.meshgrid(np.arange(xmin,xmax+dx,dx)-dx/2.,np.arange(ymin,ymax+dy,dy)-dy/2.)

'''
pcolormesh without x and y just uses indexing as labels
'''


pl.subplot(121)
pl.pcolormesh(z)
pl.title("Wrong ticks")

'''pcolormesh with x and y values gives a wrong plot, x and y are treated as boundaries'''

pl.subplot(122)
pl.title("Wrong: x,y as values")
pl.pcolormesh(x,y,z)

pl.figure()

'''using the boundaries gives correct plot'''

pl.subplot(121)
pl.title("Right: x,y as boundaries")
pl.pcolormesh(x2,y2,z)
pl.axis([x2.min(),x2.max(),y2.min(),y2.max()])

'''using the boundaries gives correct plot'''

pl.subplot(122)
pl.title("Correct ticks")
pl.pcolormesh(x2,y2,z)
pl.axis([x2.min(),x2.max(),y2.min(),y2.max()])
pl.xticks(np.arange(xmin,xmax,dx))
pl.yticks(np.arange(ymin,ymax,dy))
pl.colorbar()
pl.show()


from pylab import *  
a=arange(-2.0,2.001,1.0)  
b=arange(-2.0,2.001,1.0)  
x,y=meshgrid(a,b)  
func=lambda x,y:(x**2.0+y**4.0) 
z=func(x,y)  
pcolor(x,y,z)  
#x和y是网格,z是(x,y)坐标处的颜色值  
colorbar()#使用颜色条
show()


import numpy as np
from scipy.misc import *
 
x = np.random.random((600,800,3))
imsave('meelo.jpg', x)

