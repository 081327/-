#为X和Y轴添加注释
#主要使用xlabel,ylabel函数
import numpy
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
X=numpy.linspace(-5,5,1024)
Y=0.25*(X+4)*(X+1)*(X-2)
plt.title('Power curve')
plt.xlabel('空前速度')
plt.ylabel('Total drag')
plt.plot(X,Y,c='b')
plt.show()