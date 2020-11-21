# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 1:11
# @Author  : Yang
# @Email   : 843113495a@gmail.com
# @File    : 11. subplot多合一显示.py
# @Software: PyCharm
import matplotlib.pyplot as plt


plt.figure(num=1)
# subplot(2, 2, 1)表示把这个figure分为2行2列，并处于第一个的位置
plt.subplot(2, 2, 1)
plt.plot([0, 1], [0, 1])


# subplot(2, 2, 1)表示把这个figure分为2行2列，并处于第二个的位置
plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 1])

# 223会被识别为(2, 2, 3)
# subplot(2, 2, 1)表示把这个figure分为2行2列，并处于第三个的位置
plt.subplot(223)
plt.plot([0, 1], [0, 1])

# 224会被识别为(2, 2, 4)
# subplot(2, 2, 1)表示把这个figure分为2行2列，并处于第四个的位置
plt.subplot(224)
plt.plot([0, 1], [0, 1])


plt.figure(num=2)
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 1])
plt.show()
