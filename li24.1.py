#使用plot函数绘制一条一元二次方程的曲线，并使用savefig函数将这条曲线保存到result.jpg文件中
#使用plot函数
import matplotlib.pyplot as plt
#生成200个点的X坐标
X=range(-100,101)
#生成200个点的Y坐标
Y=[x**2 for x in X]
#绘制一元二次曲线
plt.plot(X,Y)
#将一元二次曲线保存为result1.jpg
#plt.savefig('result1.jpg')
#显示绘制的曲线
plt.show()