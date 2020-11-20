# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : 6. tick 能见度.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 0.1 * x

plt.figure()
# 设置了为数值为1的图层
plt.plot(x, y, linewidth=10, zorder=1)
plt.ylim(-2, 2)

ax = plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.spines["bottom"].set_position(("data", 0))
ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data", 0))

# 如果不添加一下操作，可以看见线条遮挡住了坐标轴上的ticks
for label in ax.get_xticklabels() + ax.get_yticklabels():
    # 先获取x轴和y轴上的所有刻度，然后设置图层为2, 字体大小为12，最后给每个刻度设置一个底色为白色，没有黑色边框，不透明度为0.7的背景box
    label.set_zorder(2)
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))

plt.show()
