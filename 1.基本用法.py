# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : 基本用法.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np

"""pycharm从2017.3版之后,将matplotlib的绘图的结果默认显示在SciView窗口中, 而不是弹出独立的窗口
    如果不喜欢这种设置,可以通过如下方式修改,弹出独立窗口
    File | Settings | Tools | Python Scientific | Show plots in toolwindow
    然后取消勾选
"""

# 生成-1到1的50个点
x = np.linspace(-1, 1, 50)
# y = x ** 2
y = 2 * x + 1

plt.plot(x, y)
plt.show()
