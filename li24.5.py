#绘制直方图和盒状图
#使用randn函数
#直方图hist()函数
#盒状图boxplot()函数
import numpy as np
import matplotlib.pyplot as plt
#产生100个正态分布的随机数
#np.random.randn()函数可以返回一个或一组服从标准正态分布的随机样本值。
data=np.random.randn(100)
print(data)
#计算100个随机数的平均值
print(np.average(data))
#在同一个窗口创建两个二维坐标系，左侧的坐标系显示直方图，右侧的坐标系显示盒状图
#subplots后面的1，2代表图是一行两列的一个呈现
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(8,8))
#绘制直方图
ax1.hist(data,100)
#绘制盒状图
ax2.boxplot(data)
#显示直方图和盒状图
plt.show()