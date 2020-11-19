# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : figure 图像.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np

"""定义不同的figure窗口"""
x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x**2

# 定义一个figure, num=1表明这个窗口名字是figure1
# 定义在某个figure之后的东西，都属于这个figure的操作
plt.figure(num=1)
# 属于figure1的操作
plt.plot(x, y1)

plt.figure(num=3)
# 属于figure3的操作
plt.plot(x, y2)

plt.show()
