#在坐标系上显示标题
import numpy
import matplotlib.pyplot as plt
#如果标题包含中文字符，要加上如下的代码
plt.rcParams['font.sans-serif']=['SimHei']  #运行配置参数中的字体（font）为黑体（SimHei）
X=numpy.linspace(-4,-4,1024)
Y=0.25 * (X+4) * (X+1) * (X-2)
plt.title('多项式曲线')
plt.plot(X,Y,c='r')
plt.show()
