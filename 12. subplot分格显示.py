# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : 12. subplot分格显示.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# method 1: subplot2grid
plt.figure(num=1)
# 把这个plot分为3 * 3 , 然后从(0,0)出发，占了1行3列
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
ax1.plot([1, 2], [1, 2])
# 以前plot的用法在前面加个set基本可以迁移到subplot上
ax1.set_title("ax1_title")

# colspan 和 rowspan的默认值是1
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax2.set_title("ax2_title")
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax3.set_title("ax3_title")
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.set_title("ax4_title")
ax5 = plt.subplot2grid((3, 3), (2, 1))
ax5.set_title("ax5_title")
# method 2: gridspec
# 和方法1类似，只是定位的方式更换成了索引的方式
plt.figure(num=2)
gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, :2])
ax3 = plt.subplot(gs[1:, 2])
ax4 = plt.subplot(gs[-1, 0])
ax5 = plt.subplot(gs[-1, -2])


# method3: easy to define structure
# 咋感觉这种方法更复杂些，以后想了解的话看源码的说明吧
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
ax11.scatter([1, 2], [1, 2])


plt.tight_layout()
plt.show()
