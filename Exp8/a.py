# coding=utf-8
#导入相应的库
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#设置字体，可以在图上显示中文
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
#读取数据
data=pd.read_excel('海外疫情.xlsx',index_col=0)
#数据计算，这里只取前20个国家
radius = data['累计'][:20]
n=radius.count()
theta = np.arange(0, 2*np.pi, 2*np.pi/n)+2*np.pi/(2*n)    #360度分成20分，外加偏移
#在画图时用到的 plt.cm.spring_r(r)   r的范围要求时[0,1]
radius_maxmin=(radius-radius.min())/(radius.max()-radius.min())  #x-min/max-min   归一化
#画图
fig = plt.figure(figsize=(20,5),dpi=256)
ax = fig.add_subplot(projection='polar')    #启用极坐标
bar = ax.bar(theta, radius,width=2*np.pi/n)
ax.set_theta_zero_location('N')  #分别为N, NW, W, SW, S, SE, E, NE
ax.set_rgrids([])    #用于设置极径网格线显示
# ax.set_rticks()    #用于设置极径网格线的显示范围
# ax.set_theta_direction(-1)    #设置极坐标的正方向
ax.set_thetagrids([])  #用于设置极坐标角度网格线显示
# ax.set_theta_offset(np.pi/2)       #用于设置角度偏离
ax.set_title('新冠肺炎全球疫情形势',fontdict={'fontsize':8})   #设置标题
#设置扇形各片的颜色
for r, bar in zip(radius_maxmin, bar):
    bar.set_facecolor(plt.cm.spring_r(r))
    bar.set_alpha(0.8)
#设置边框显示
for key, spine in ax.spines.items():
    if key=='polar':
        spine.set_visible(False)
plt.show()
#保存图片
fig.savefig('COVID.png')