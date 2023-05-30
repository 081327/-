#定制曲线类型
import numpy
import matplotlib.pyplot as plt
X=numpy.linspace(-6,-6,1024)
#设置曲线类型为实线
plt.plot(X,-X**2,color='r',linestyle='solid')
#设置曲线类型为虚线
plt.plot(X,-X**2 + 3,color='b',linestyle='dashed')
#设置曲线类型为点画线
plt.plot(X,-X**2 + 6,color='k',linestyle='dashdot')
plt.show()