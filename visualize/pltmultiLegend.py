#encoding:utf-8
# 导入matplotlib.pyplot, numpy 包
import numpy as np
import matplotlib.pyplot as plt

# 添加主题样式
# plt.style.use('mystyle')
# 设置图的大小，添加子图
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)
#绘制sin, cos
x = np.arange(-np.pi, np.pi, np.pi / 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3=np.tan(x)
sin, = ax.plot(x, y1, color='red', label='sin')
cos, = ax.plot(x, y2, color='blue', label='cos')
tan, = ax.plot(x, y2, color='black', label='tan')


ax.set_ylim([-1.2, 1.2])
# 第二种方式 拆分显示
sin_legend = ax.legend(handles=[sin,tan], loc='upper right')
ax.add_artist(sin_legend)
ax.legend(handles=[cos], loc='lower right')
plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
#添加主题样式
# plt.style.use('mystyle')
#设置图的大小，添加子图
# fig = plt.figure(figsize=(5,5))
# ax = fig.add_subplot(111)
# for color in ['red', 'green']: 
    # n = 750 
    # x, y = np.random.rand(2, n) 
    # scale = 200.0 * np.random.rand(n) 
    # ax.scatter(x, y, c=color, s=scale, r
                # label=color, alpha=0.3, 
                # edgecolors='none')
# ax.legend() 
# ax.grid(True)
# plt.show()