# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : 3. 设置坐标轴上.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# 设置x轴的取值范围是-1到2
plt.xlim((-1, 2))
# 设置y轴的取值范围是-2到3
plt.ylim((-2, 3))
# 设置x轴的描述
plt.xlabel("I am x")
# 设置y轴的描述
plt.ylabel("I am y")

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
# 更换x轴上的单位小标
plt.xticks(new_ticks)
# 更换y轴上的单位小标， y轴上的really bad 就对应的是-2， really good 就对应的是3
# plt.yticks([-2, -1.8, -1, 1.22, 3], ['really bad', 'bad', 'normal', 'good', 'really good'])
# 在进一步更换一个看起来更好的字体，数学形式的字体
# 例子中具体操作就是先添加一个转义符r, 然后再各个ticks前后添加美元符$, 如果中间有空格要用反斜杠\加空格代替
# 具体的语法可以参考latex
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])


# 改变坐标轴的位置
# gca 是 get current axis的缩写
# 获得figure的边框(共上下左右四个)
ax = plt.gca()
# 设置右边边框的颜色为none
ax.spines['right'].set_color('none')
# 设置上边边框的颜色为none
ax.spines['top'].set_color('none')
# 选定x轴为底部边框
ax.xaxis.set_ticks_position('bottom')
# 选定y轴为左边边框
ax.yaxis.set_ticks_position('left')
# 将x轴放在y轴的0处
ax.spines['bottom'].set_position(('data', 0))
# 将y轴放在x轴的0处
ax.spines['left'].set_position(('data', 0))

plt.show()
