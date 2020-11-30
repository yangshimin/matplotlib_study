# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : 13. 图中图.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fg = plt.figure(num=1)
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fg.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2 = fg.add_axes([left, bottom, width, height])
ax2.plot(y, x, 'r')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 2')

plt.axes([.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title("title inside 2")


plt.show()
