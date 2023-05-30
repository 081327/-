#绘制随机点
#使用scatter函数
import random
import matplotlib.pyplot as plt
count=1024
#注意：随机参数1024个随机点的X坐标值
X=[random.random()*100 for i in range(count)]
#随机参数1024个随机点的Y坐标值
Y=[random.random()*100 for i in range(count)]
#绘制1024个随机点
plt.scatter(X,Y)
#显示绘制的随机点
plt.show()
