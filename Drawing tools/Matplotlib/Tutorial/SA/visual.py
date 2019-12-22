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
# myfont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=18)
# titlefont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=14)
#图表的x轴数据，是一个可迭代的数据类型
gains_visual = [0,1,2]
estimation_visual_withtask = [- 38.33, - 62.07, 7.43]
estimation_visual_withouttask = [- 93.15, - 22.63, - 104.93]
estimation_visual_mean = [- 42.35,- 42.35,- 42.35]
stdevp_visual_withtask = [68.35, 34.99, 34.34]
stdevp_visual_withouttask = [22.85, 43.79, 33.57]
error_attri = dict(elinewidth = 2, ecolor = "black", capsize = 3)


plt.plot(gains_visual,estimation_visual_withtask, color='royalblue', linestyle='solid', linewidth=2, marker='o', markersize=4, label="With Cognitive Task")
plt.plot(gains_visual,estimation_visual_withouttask, color='orange', linestyle='dashed', linewidth=2, marker='o', markersize=4, label="Without Cognitive Task")
plt.plot(gains_visual,estimation_visual_mean, color='grey', linestyle='-', linewidth=2, alpha=0.5, marker='o', markersize=4, label="Mean")
plt.xlabel(r'Visual Gains ($g_v$)')
plt.ylabel(r'Estimation Deviation ($\overline{t_{dev}}$)')
plt.xticks(gains_visual,labels=["%s"%(i) for i in gains_visual])
plt.grid(True,axis="y",ls=":",color="gray",alpha=0.5)

plt.errorbar(gains_visual,estimation_visual_withtask,yerr=stdevp_visual_withtask,fmt='o',elinewidth=1,capsize=4, ecolor = 'royalblue', color = 'royalblue')
plt.errorbar(gains_visual,estimation_visual_withouttask,yerr=stdevp_visual_withouttask,fmt='o',elinewidth=1,capsize=4, ecolor = 'orange', color = 'orange')



for a,b in zip(gains_visual,estimation_visual_withtask):
	plt.text(a, b+0.2, '%.2f' % b, ha='center', va= 'bottom',fontsize=9)
for a,b in zip(gains_visual,estimation_visual_withouttask):
    plt.text(a, b+0.2, '%.2f' % b, ha='center', va= 'bottom',fontsize=9)
for a,b in zip(gains_visual,estimation_visual_mean):
    plt.text(gains_visual[-1], estimation_visual_mean[-1]+0.2, '%.2f' % b, ha='center', va= 'bottom',fontsize=9)    

plt.legend(loc='best')

plt.savefig('pyvisualdevdev.eps',dpi=600,format='eps')
plt.savefig('pyvisualdevdev.svg',dpi=600,format='svg')
plt.savefig('pyvisualdevdev.pdf',dpi=600,format='pdf')
plt.savefig('pyvisualdevdev.png',dpi=600,format='png')
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
