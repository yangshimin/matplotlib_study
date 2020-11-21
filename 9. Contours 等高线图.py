# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 11:20
# @Author  : Yang
# @Email   : 843113495a@gmail.com
# @File    : 9. Contours 等高线图.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2-y**2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)


# use plt.contourf to filling contours
# X, Y and value for (X, Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)

# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
# adding label
plt.clabel(C, inline=True, fontsize=10)


plt.xticks(())
plt.yticks(())

plt.show()
