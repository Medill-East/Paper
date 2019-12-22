from matplotlib import font_manager
from matplotlib import pyplot as plt
import matplotlib.ticker as mtick

# myfont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=18)
# titlefont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=14)
#图表的x轴数据，是一个可迭代的数据类型
gains_auditory = [0,1,2]
estimation_auditory_withtask = [-19.29, - 14.62, -12.86]
estimation_auditory_withouttask = [- 15.37, - 12.39, - 19.19]
estimation_auditory_mean = [- 13.50,- 13.50,- 13.50]
stdevp_auditory_withtask = [21.12, 14.18, 14.31]
stdevp_auditory_withouttask = [29.07, 22.91, 21.93]
error_attri = dict(elinewidth = 2, ecolor = "black", capsize = 3)


plt.plot(gains_auditory,estimation_auditory_withtask, color='royalblue', linestyle='solid', linewidth=2, marker='o', markersize=4, label="With Cognitive Task")
plt.plot(gains_auditory,estimation_auditory_withouttask, color='darkorange', linestyle='dashed', linewidth=2, marker='o', markersize=4, label="Without Cognitive Task")
plt.plot(gains_auditory,estimation_auditory_mean, color='grey', linestyle='-', linewidth=2, alpha=0.5, marker='o', markersize=4, label="Mean")
plt.xlabel(r'Auditory Gains ($g_a$)')
plt.ylabel(r'Estimation Deviation ($\overline{t_{dev}}$) (%)')
plt.xticks(gains_auditory,labels=["%s"%(i) for i in gains_auditory])
plt.grid(True,axis="y",ls=":",color="gray",alpha=0.5)

plt.errorbar(gains_auditory,estimation_auditory_withtask,yerr=stdevp_auditory_withtask,fmt='o',elinewidth=1,capsize=4, ecolor = 'royalblue', color = 'royalblue')
plt.errorbar(gains_auditory,estimation_auditory_withouttask,yerr=stdevp_auditory_withouttask,fmt='o',elinewidth=1,capsize=4, ecolor = 'darkorange', color = 'darkorange')

fmt='%.0f%%'
yticks = mtick.FormatStrFormatter(fmt)
# plt.yaxis.set_major_formatter(yticks)
plt.gca().yaxis.set_major_formatter(yticks)

for a,b in zip(gains_auditory,estimation_auditory_withtask):
	plt.text(a+0.12, b+1, '%.2f' % b, ha='center', va= 'bottom',fontsize=9, color='royalblue', weight='bold')
for a,b in zip(gains_auditory,estimation_auditory_withouttask):
    plt.text(a+0.12, b+1.5, '%.2f' % b, ha='center', va= 'bottom',fontsize=9, color='darkorange', weight='bold')
for a,b in zip(gains_auditory,estimation_auditory_mean):
    plt.text(gains_auditory[-1]+0.12, estimation_auditory_mean[-1], '%.2f' % b, ha='center', va= 'bottom',fontsize=9, color='grey', weight='bold')    

plt.legend(loc='best')

plt.savefig('pyauditorydevdev.eps',dpi=600,format='eps',bbox_inches = 'tight')
# plt.savefig('pyauditorydevdev.svg',dpi=600,format='svg',bbox_inches = 'tight')
# plt.savefig('pyauditorydevdev.pdf',dpi=600,format='pdf',bbox_inches = 'tight')
plt.savefig('pyauditorydevdev.png',dpi=600,format='png',bbox_inches = 'tight')

plt.show()



