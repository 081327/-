#定制柱状图的填充模式
import numpy
import matplotlib.pyplot as plt
N=8
A=numpy.random.random(N)
B=numpy.random.random(N)
#设置柱状图下半部分的填充模式为“x”
plt.bar(range(N),A,color='b',hatch='x')
#设置柱状图上半部分的填充模式为“*”
plt.bar(range(N),A+B,bottom=A,color='r',hatch='*')
plt.show()