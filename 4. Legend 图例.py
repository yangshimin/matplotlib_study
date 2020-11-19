# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19
# @Author  : YangShiMin
# @Email   : fausty@synnex.com
# @File    : Legend 图例.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 50)
y1 = 3*x + 1
y2 = x**2

plt.figure()
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

# 为这条曲线添加描述，名为up
line_one, = plt.plot(x, y2, label='up')
# 为这条曲线添加描述，名为down
line_two, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')
# 设置图例
# plt.legend()
# 还有一些更灵活的用法
# handles表示要对哪些曲线添加图例，labels是和handles中相对应的曲线描述, 同时还会覆盖之前定义的up 和 down
# loc 表示图例要在什么地方显示;
# best: 会自动找一个不影响数据展示的地方显示图例; 还有其他的显示位置如：upper right、center left、center等等
# title: 图例的title
plt.legend(handles=[line_one, line_two], labels=['aaaa', 'bbbb'], loc='best', title="matplotlib_study")

plt.show()
