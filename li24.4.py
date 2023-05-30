#绘制柱状图
#bar函数
import matplotlib.pyplot as plt
#[1980,1985,1990,1995]表示X坐标序列
# [1000,3000,4000,5000]表示Y坐标序列
#width=3表示柱的宽度
plt.bar([1980,1985,1990,1995],[1000,3000,4000,5000],width=3)
plt.show()