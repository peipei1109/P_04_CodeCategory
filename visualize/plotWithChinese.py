# -*- encoding: utf-8 -*-
'''
Created on 2016年7月4日

@author: LuoPei
'''

from matplotlib.font_manager import FontProperties

import matplotlib.pyplot as plt

#下面是一段测试代码，在可视化中加上英文标注~~~
font_peipei_consolas = FontProperties(fname="STSONG.TTF")
x = range(10)
plt.plot(x)
plt.title(u"中文",fontproperties=font_peipei_consolas, fontsize=14)#记得写中文的时候前面加上u
plt.show()
