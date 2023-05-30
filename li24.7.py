#定制曲线颜色
#使用plot函数中的color关键字参数
import numpy
import matplotlib.pyplot as plt
#将-6到6分成1024份，形成1024个值
X=numpy.linspace(-6,6,1024)
#定义曲线的颜色集合，所有的颜色都从这个列表中选取
colors=['red','yellow','b','c','#FF00FF','0.75']
#绘制20条一元二次曲线，并从colors中依次取颜色值
for i in range(20):
    plt.plot(X,-X**2 + (i+1)*2,color=colors[i % len(colors)])
    #显示20条曲线
    plt.show()
