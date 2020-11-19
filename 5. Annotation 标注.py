# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : 5. Annotation 标注.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure(num=1, figsize=(8, 5))
plt.plot(x, y)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))


x0 = 1
y0 = 2*x0 + 1
# 散点, size为50， 颜色为blue
plt.scatter(x0, y0, s=50, color='b')
# 设置两点之间的线条格式
# 第一个参数是表示横坐标，第二个参数是表示纵坐标；所以[x0, x0]，[y0, 0]代表的是(x0, y0)和(x0, 0)这两个点
# k--: 线条颜色为黑色black, -- 表示用虚线表示
# lw: 线条的宽度为2.5
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)


# method 1
# xy: 标注点的坐标; xycoords: 标注点的坐标系; xytext: 标记的左下角点的位置, textcoords:坐标系(这里是相对坐标系);
# fontsize:字体大小; arrowsprops: 是一个描述标注指向标注点的方式
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))


# method 2
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text.\ mu\ \sigma_i\ \alpha_t$', fontdict={"size":16, "color": "r"})

plt.show()
