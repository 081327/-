#绘制正弦或余弦曲线
#使用plot函数
#用到numpy.linspace函数 
import math
import matplotlib.pyplot as plt
import numpy
#将0到2Π分成100份3，以Numpy数组形式返回这100个X值
X=numpy.linspace(0,2*numpy.pi,100)   #numpy.linspace()后面括号里面的分别为起始数，终点数，中间分割的点数
Y=numpy.sin(X)
plt.plot(X,Y)
plt.show()
