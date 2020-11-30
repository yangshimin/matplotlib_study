# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : 15. Animation 动画.py
# @Software: PyCharm
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x+i/100))
    return line,


def init():
    line.set_ydata(np.sin(x))
    return line,


#  frames: 帧数; init_func: 最开始的动画效果是什么样的; interval: 频率，动画更新的时间间隔; blit:是否整个图形的点，还是更新变化的哪些点
ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=True)

plt.show()
