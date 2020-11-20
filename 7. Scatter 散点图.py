# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : 7. Scatter 散点图.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np

n = 1024
# 标准正态
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
# numpy.arctan(x): ndarry—每个元素的范围为(-π/2,π/2)
# numpy.arctan2(x1,x2): 返回值的范围为[-π,+π]
T = np.arctan2(Y, X)   # for color value

# 绘制散点图, 大小为75, color为T, 不透明度为0.5
plt.scatter(X, Y, s=75, c=T, alpha=0.5)

# 设置X轴的范围是-1.5~1.5
plt.xlim((-1.5, 1.5))
# 设置Y轴的范围是-1.5~1.5
plt.ylim((-1.5, 1.5))

# 隐藏x轴的刻度
plt.xticks(())
# 隐藏Y轴的刻度
plt.yticks(())

plt.show()
