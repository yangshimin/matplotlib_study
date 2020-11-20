# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : 8. Bar 柱状图.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
# 根据X，对Y产生一些随机变量
# uniform: 从一个均匀分布[low, high)中随机采样，定义域是左闭右开
Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)

# 因为Y在此处是个正数，所以 +Y1: 表示向上的柱状图; -Y2: 表示向下的柱状图
# 分别设置主体颜色facecolor和边框颜色edgecolor
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

# ha: 横向对齐的方式
# va: 纵向对齐的方式
for x, y in zip(X, Y1):
    plt.text(x, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    plt.text(x, -y-0.05, '-%.2f' % y, ha='center', va='top')

plt.xlim(-.5, n)
# 隐藏X轴的刻度
plt.xticks(())
plt.ylim(-1.25, 1.25)
# 隐藏Y轴的刻度
plt.yticks(())

plt.show()
