'''
Date: 01/10/2020
Author: Raihan Sayeed Khan
A function written to easily change the fontname, fontsize, and number of minor ticks of a python plot
'''
# function start
# input axis object, the x and y-axis labels, and the title (optional) of the plot
def pretty_plot(ax, xlabel, ylabel, title = ''):
    from matplotlib.ticker import AutoMinorLocator
    from matplotlib import font_manager
    
#    font_name = 'Times New Roman'
    font_name = 'Helvetica'
    label_fontsize = 18
    tick_fontsize = 16
    title_fontsize = 18
    no_of_minor_ticks = 1
    legend_fontsize = 16

    # setting axis labels
    title_font = {'fontfamily': font_name,'fontsize': title_fontsize, 'fontweight': 'bold'}
    axis_font = {'fontfamily': font_name,'fontsize': label_fontsize, 'fontweight': 'normal'}
    ax.set_xlabel(xlabel, fontdict=axis_font)
    ax.set_ylabel(ylabel, fontdict=axis_font)
    
    # setting title
    ax.set_title(title, fontdict=title_font)

    # setting minor ticks
    ax.xaxis.set_minor_locator(AutoMinorLocator(no_of_minor_ticks+1))
    ax.yaxis.set_minor_locator(AutoMinorLocator(no_of_minor_ticks+1))

    # setting tick properties
    ticks_font = font_manager.FontProperties(family=font_name, size=tick_fontsize, weight='normal')
    for tick in ax.get_xticklabels():
        tick.set_fontproperties(ticks_font)
    for tick in ax.get_yticklabels():
        tick.set_fontproperties(ticks_font)
        
    # legend
#    ax.legend(prop={'family':font_name, 'size':legend_fontsize},bbox_to_anchor=[0.6, 1])
    ax.legend(prop={'family':font_name, 'size':legend_fontsize},loc = 'upper left')

# function end
       
# main code       
import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir(r'D:\Gdrives\sort_and_store_gdrive\github\python_plot')
savedir = os.getcwd()

figname = 'plot'
xmin = 0
xmax = 10
ymin = 0
ymax = 10
title1 = 'With formatting function'
title2 = 'By Default'
xlabel = 'x-axis'
ylabel = 'y-axis'

#xticks = np.arange(0,10.1, 2)
#yticks = np.arange(0,10.1, 2)
data = np.arange(1, 11, 1)

# plotting two subplots in a row to make comparison
fig = plt.figure(figsize = (12, 4)) 		# w x h in inches
# figure with formatting funciton
ax1 = fig.add_subplot(122)
ax1.plot(data, data, label = 'sample data', color='red', marker='o', linestyle='solid', linewidth=2, markersize=12, markeredgewidth = 1, markeredgecolor = 'black', markerfacecolor = 'red', ) 		
pretty_plot(ax= ax1, xlabel=xlabel, ylabel=ylabel, title = title1)

# figure with just plot options
ax2 = fig.add_subplot(121)
ax2.plot(data, data, label = 'sample data', color='red', marker='o', linestyle='solid', linewidth=2, markersize=12, markeredgewidth = 1, markeredgecolor = 'black', markerfacecolor = 'red', ) 		
ax2.set_title(title2)

plt.show()
fig.savefig(savedir+'\\'+figname+'.png', bbox_inches='tight', dpi = 300)        # saving the figure
plt.close(fig)