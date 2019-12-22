# import random
# from matplotlib import pyplot as plt
# from matplotlib import font_manager

# x_age = range(11, 31)
# y_count_1 = [random.randint(0, 5) for i in range(20)]
# y_count_2 = [random.randint(0, 5) for j in range(20)]
# myfont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=14)
# titlefont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=20)

# plt.figure(figsize=(10, 10))

# # 在同一个图里面绘制多条折线,
# #  color: 线条颜色
# #  linestyle： 线条的风格
# #  linewidth: 线条的粗细
# #  alpha: 透明度
# plt.plot(x_age, y_count_1, color='g', linestyle='-.', linewidth=5, alpha=0.5, label="自己")
# plt.plot(x_age, y_count_2, color='r', linestyle='--', linewidth=3, alpha=0.3, label="同桌")

# # 添加图例
# plt.legend(loc="upper right", prop=titlefont)

# # 添加网格
# plt.grid(alpha=0.3)

# plt.title("11岁至30岁所交男(女)友个数", fontproperties=titlefont)
# plt.xlabel("年龄", fontproperties=myfont)
# plt.ylabel("女(男)友数量", fontproperties=myfont)


# plt.xticks(x_age, labels=["%s岁" %(item) for item in x_age], fontproperties=myfont, rotation=45)
# plt.scatter(x_age[0], y_count_1[0], c='r')

# plt.legend(loc='best')

# plt.show()

from matplotlib import font_manager
from matplotlib import pyplot as plt

import matplotlib.ticker as mtick



# myfont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=18)
# titlefont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=14)
#图表的x轴数据，是一个可迭代的数据类型
gains_visual = [0,1,2]
estimation_visual_withtask = [- 6.24, - 10.10, 1.21]
estimation_visual_withouttask = [- 15.17, - 3.68, - 17.09]
estimation_visual_mean = [- 6.89,- 6.89,- 6.89]
stdevp_visual_withtask = [33.40, 21.32, 14.79]
stdevp_visual_withouttask = [13.42, 20.17, 20.45]
error_attri = dict(elinewidth = 2, ecolor = "black", capsize = 3)
percentage = ['%','%','%']

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

plt.plot(gains_visual,estimation_visual_withtask, color='royalblue', linestyle='solid', linewidth=2, marker='o', markersize=4, label="高认知负载")
plt.plot(gains_visual,estimation_visual_withouttask, color='darkorange', linestyle='dashed', linewidth=2, marker='o', markersize=4, label="低认知负载")
plt.plot(gains_visual,estimation_visual_mean, color='grey', linestyle='-', linewidth=2, alpha=0.5, marker='o', markersize=4, label="均值")
plt.xlabel(r'视觉授时因子 ($g_v$)')
plt.ylabel(r'时间估计偏差百分比 ($\overline{t_{dev}}$) (%)')
plt.xticks(gains_visual,labels=["%s"%(i) for i in gains_visual])
plt.grid(True,axis="y",ls=":",color="gray",alpha=0.5)

plt.errorbar(gains_visual,estimation_visual_withtask,yerr=stdevp_visual_withtask,fmt='o',elinewidth=1,capsize=4, ecolor = 'royalblue', color = 'royalblue')
plt.errorbar(gains_visual,estimation_visual_withouttask,yerr=stdevp_visual_withouttask,fmt='o',elinewidth=1,capsize=4, ecolor = 'darkorange', color = 'darkorange')

fmt='%.0f%%'
yticks = mtick.FormatStrFormatter(fmt)
# plt.yaxis.set_major_formatter(yticks)
plt.gca().yaxis.set_major_formatter(yticks)

for a,b in zip(gains_visual,estimation_visual_withtask):
	plt.text(a+0.1, b+1, '%.2f' % b, ha='center', va= 'bottom',fontsize=9, color='royalblue', weight='bold')
for a,b in zip(gains_visual,estimation_visual_withouttask):
    plt.text(a+0.1, b+1, '%.2f' % b, ha='center', va= 'bottom',fontsize=9, color='darkorange', weight='bold')
for a,b in zip(gains_visual,estimation_visual_mean):
    plt.text(gains_visual[-1]+0.1, estimation_visual_mean[-1]+1, '%.2f' % b, ha='center', va= 'bottom',fontsize=9, color='grey', weight='bold')    

plt.legend(loc='best')

plt.savefig('pyvisualdevdev.eps',dpi=600,format='eps',bbox_inches = 'tight')
# plt.savefig('pyvisualdevdev.svg',dpi=600,format='svg',bbox_inches = 'tight')
# plt.savefig('pyvisualdevdev.pdf',dpi=600,format='pdf',bbox_inches = 'tight')
plt.savefig('pyvisualdevdev.png',dpi=600,format='png',bbox_inches = 'tight')
plt.show()




# x_times = [0,1,2]
# #图表的y轴数据是一个可迭代数据类型
# y_temp = [-93.15, 11, 12, 22, 32, 33, 31, 41,54, 35, 56, 14]

# plt.figure(figsize=(10, 10))
# #传入x和y轴的数据，绘制图形
# plt.plot(x_times, y_temp)
# plt.title("每天的气温变化(每隔两个小时)", fontproperties=titlefont)
# plt.xlabel("时间", fontproperties=myfont )
# plt.ylabel("温度", fontproperties=myfont)
# plt.xticks(x_times,labels=["%s时"%(i) for i in x_times], fontproperties=myfont)
# plt.savefig('doc/temp.png')
# #在执行程序时显示图像

# plt.legend(loc='best')

# plt.show()
