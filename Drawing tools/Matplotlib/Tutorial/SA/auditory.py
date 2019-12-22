from matplotlib import font_manager
from matplotlib import pyplot as plt
# myfont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=18)
# titlefont = font_manager.FontProperties(fname="/usr/share/fonts/cjkuni-uming/uming.ttc", size=14)
#图表的x轴数据，是一个可迭代的数据类型
gains_auditory = [0,1,2]
estimation_auditory_withtask = [- 127.38, - 92.33, -80.00]
estimation_auditory_withouttask = [- 94.64, - 77.09, - 123.23]
estimation_auditory_mean = [- 84.71,- 84.71,- 84.71]
stdevp_auditory_withtask = [- 37.86,- 25.97,- 28.17]
stdevp_auditory_withouttask = [55.06, 42.73, 38.61]
error_attri = dict(elinewidth = 2, ecolor = "black", capsize = 3)


plt.plot(gains_auditory,estimation_auditory_withtask, color='royalblue', linestyle='solid', linewidth=2, marker='o', markersize=4, label="With Cognitive Task")
plt.plot(gains_auditory,estimation_auditory_withouttask, color='orange', linestyle='dashed', linewidth=2, alpha=0.5, marker='o', markersize=4, label="Without Cognitive Task")
plt.plot(gains_auditory,estimation_auditory_mean, color='grey', linestyle='-', linewidth=2, alpha=0.5, marker='o', markersize=4, label="Mean")
plt.xlabel(r'Auditory Gains ($g_a$)')
plt.ylabel(r'Estimation Deviation ($\overline{t_{dev}}$)')
plt.xticks(gains_auditory,labels=["%s"%(i) for i in gains_auditory])
plt.grid(True,axis="y",ls=":",color="gray",alpha=0.5)

plt.errorbar(gains_auditory,estimation_auditory_withtask,yerr=stdevp_auditory_withtask,fmt='o',elinewidth=1,capsize=4, ecolor = 'royalblue', color = 'royalblue')
plt.errorbar(gains_auditory,estimation_auditory_withouttask,yerr=stdevp_auditory_withouttask,fmt='o',elinewidth=1,capsize=4, ecolor = 'orange', color = 'orange')



for a,b in zip(gains_auditory,estimation_auditory_withtask):
	plt.text(a, b+0.2, '%.2f' % b, ha='center', va= 'bottom',fontsize=9)
for a,b in zip(gains_auditory,estimation_auditory_withouttask):
    plt.text(a, b+0.2, '%.2f' % b, ha='center', va= 'bottom',fontsize=9)
for a,b in zip(gains_auditory,estimation_auditory_mean):
    plt.text(gains_auditory[-1], estimation_auditory_mean[-1]+0.2, '%.2f' % b, ha='center', va= 'bottom',fontsize=9)    

plt.legend(loc='best')

plt.savefig('pyauditorydevdev.eps',dpi=600,format='eps')
plt.savefig('pyauditorydevdev.svg',dpi=600,format='svg')
plt.savefig('pyauditorydevdev.pdf',dpi=600,format='pdf')
plt.savefig('pyauditorydevdev.png',dpi=600,format='png')

plt.show()



