#使用LaTex格式的标题
import numpy
import matplotlib.pyplot as plt
X=numpy.linspace(-4,-4,1024)
Y=0.25*(X+4)*(X+1)*(X-2)
#设置LaTex格式的标题
plt.title(r'$f(x) =\frac{1}{4}(x+4)(x+1)(x-2)$')  #\frac{}{}为分数形式，这个表示1/4
plt.plot(X,Y,c='b')
plt.show()
