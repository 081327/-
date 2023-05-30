#为文本注释添加Box
#使用bbox关键字参数
import numpy
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
X=numpy.linspace(-5,5,1024)
Y=0.25*(X+4)*(X+1)*(X-2)
box={
     'facecolor':'0.75',
     'edgecolor':'b',
     'boxstyle':'round'
}
#设置注释文本的样式
plt.text(-0.5,-0.2,'abcde',bbox=box)
plt.plot(X,Y,c='r')
plt.show()