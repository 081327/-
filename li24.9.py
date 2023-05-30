#定制柱状颜色
import random
import matplotlib.pyplot as plt
#随机产生50个0到99的随机数，同于X轴的坐标值（相当于Y随机从0-99之间随机产生）
values=[random.randint(0,99) for i in range(50)]
#颜色会从这个列表中获取
color_set=['#FF00FF','#FFFF00','r','b']
#产生50个颜色值的列表
color_list=[color_set[random.randint(0,3)] for i in range(50)]   #注意：这块必须是用[],因为是列表形式
#用多种颜色绘制柱状图
plt.bar(range(len(values)),values,color=color_list)
plt.show()