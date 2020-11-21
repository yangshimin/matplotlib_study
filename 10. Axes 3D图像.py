# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 12:00
# @Author  : Yang
# @Email   : 843113495a@gmail.com
# @File    : 10. Axes 3D图像.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
# 将figure 变为3D
ax = Axes3D(fig)

X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
# np.meshgrid: 生成网格点坐标矩阵
# https://blog.csdn.net/lllxxq141592654/article/details/81532855
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
# 计算Z轴的高度
Z = np.sin(R)


# rstride:行之间的跨度
# cstride:列之间的跨度
# cmap是颜色映射表
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap("rainbow"))
# 绘制从3D曲面到底部的投影,zdir 可选 'z'|'x'|'y'| 分别表示投影到z,x,y平面
# zdir = 'z', offset = -2 表示投影到z = -2上
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap="rainbow")
ax.set_zlim(-2, 2)


plt.show()
