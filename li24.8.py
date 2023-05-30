#定制离散点的样式
import numpy
import matplotlib.pyplot as plt
#产生第一组标准正态分布的随机数，100是Numpy数组元素的个数，2是数组的维度
A=numpy.random.standard_normal((100,2))
#将A数组中的每一个值都加-1
A+=numpy.array((-1,-1))
#产生第二组标准正态分布的随机数
B=numpy.random.standard_normal((100,2))
#将B数组中的每一个值都加1
B+=numpy.array((1,1))
#设置离散点要用到的颜色
colors=['red','yellow','b','c','#FF00FF','0,75']
#取A和B不同的列绘制离散点
plt.scatter(A[:,0],A[:,1],color=colors[0])   #注意：这块的，千万别忘了
plt.scatter(B[:,0],B[:,1],color=colors[2])
#修改离散点的默认样式
plt.scatter(A[:,0],B[:,1],color=colors[4],edgecolor=colors[2],s=200,linewidths=3)   #s代表面积
plt.show()