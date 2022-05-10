
from matplotlib import pyplot as plt
import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import os
import csv


# data_path = pd.read_csv("SPY.csv")
data_path = pd.read_csv("/Users/pw/final-project-Pengchao_Wang/SPY.csv")
#print(data_path)

#911_inside
start_911 = datetime.datetime(2001, 9, 1)

end_911 = datetime.datetime(2002, 9, 1)

df_911 = web.DataReader("SPY", 'yahoo', start_911, end_911)

#print(df_911)

#Iraq war_outside
start_Iraq_war = datetime.datetime(2003, 3, 20)

end_Iraq_war = datetime.datetime(2004, 3, 20)

df_Iraq_war = web.DataReader("SPY", 'yahoo', start_Iraq_war, end_Iraq_war)

#print(df_Iraq_war)


#mavg_911
close_911 = df_911['Adj Close']

mavg_911 = close_911.rolling(window=100).mean()

#print(mavg_911)

# mavg_Iraq_war
close_Iraq_war = df_Iraq_war['Adj Close']

mavg_Iraq_war = close_Iraq_war.rolling(window=100).mean()

#print(mavg_Iraq_war)


# show the plot
font1 = {'family':'serif','color':'red','size':15}

def plot_911():
	plt.title('911 mavg', fontdict = font1)
	plt.xlabel("Years")
	close_911.plot()
	mavg_911.plot()
	plt.savefig('911_mavg.png')
	plt.show()
	plt.close()
	


def plot_Iraq_war():
    plt.title('Iraq_war mavg', fontdict = font1)
    close_Iraq_war.plot()
    mavg_Iraq_war.plot()
    plt.savefig('Iraq_war_mavg.png')
    plt.show()
    plt.close()
    
 



# return

def return_911():
    rets = close_911 / close_911.shift(1) - 1
    plt.title('911 return', fontdict = font1)
    rets.plot(label='return')
    plt.savefig('return_911.png')
    plt.show()
    plt.close()

def return_Iraq_war():  
    rets = close_Iraq_war / close_Iraq_war.shift(1) - 1
    plt.title('Iraq_war return', fontdict = font1)
    rets.plot(label='return')
    plt.savefig('return_Iraq_war.png')
    plt.show()
    plt.close()


# DJI(DIA), IXIC(QQQ) during 911
dfcom_911 = web.DataReader(['SPY', 'DIA', 'QQQ'],'yahoo',start=start_911,end=end_911)['Adj Close']

def plot_DIAQQQ_911():
	retscomp = dfcom_911.pct_change()
	plt.scatter(retscomp.DIA, retscomp.QQQ)
	plt.xlabel('Returns DIA')
	plt.ylabel('Returns QQQ')
	plt.title('911 DIA & QQQ', fontdict = font1)
	plt.savefig('911_DIAQQQ_return.png')
	plt.show()
	plt.close()

#Stock returns and risk

def plot_911_risk():
    retscomp = dfcom_911.pct_change()
    plt.scatter(retscomp.mean(), retscomp.std())
    plt.xlabel('Expected returns')
    plt.ylabel('Risk')
    for label, x, y in zip(retscomp.columns, retscomp.mean(), retscomp.std()):
        plt.annotate(label,xy = (x, y), xytext = (20, -20),textcoords = 'offset points', ha = 'right', va = 'bottom',bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3,rad=0'))
    
    plt.title('911 risk', fontdict = font1)
    plt.savefig('911_risk.png')
    plt.show()
    plt.close()

# KDE
def plot_911_KDE():
    retscomp = dfcom_911.pct_change()
    corr = retscomp.corr()
    plt.imshow(corr, cmap='hot', interpolation='none')
    plt.colorbar()
    plt.xticks(range(len(corr)), corr.columns)
    plt.yticks(range(len(corr)), corr.columns)
    plt.title('911 correlation kde', fontdict = font1)
    plt.savefig('911_correlation kde.png')
    plt.show()
    plt.close()
 



# DJI(DIA), IXIC(QQQ) during Iraq_war
dfcom_Iraq_war = web.DataReader(['SPY', 'DIA', 'QQQ'],'yahoo',start=start_Iraq_war,end=end_Iraq_war)['Adj Close']

def plot_DIAQQQ_Iraq_war():
	retscomp = dfcom_Iraq_war.pct_change()
	plt.scatter(retscomp.DIA, retscomp.QQQ)
	plt.xlabel('Returns DIA')
	plt.ylabel('Returns QQQ')
	plt.title('Iraq_war DIA & QQQ', fontdict = font1)
	plt.savefig('Iraq_war_DIAQQQ_return.png')
	plt.show()
	plt.close()

#Stock returns and risk
def plot_Iraq_war_risk():
    retscomp = dfcom_Iraq_war.pct_change()
    plt.scatter(retscomp.mean(), retscomp.std())
    plt.xlabel('Expected returns')
    plt.ylabel('Risk')
    for label, x, y in zip(retscomp.columns, retscomp.mean(), retscomp.std()):
        plt.annotate(label,xy = (x, y), xytext = (20, -20),textcoords = 'offset points', ha = 'right', va = 'bottom',bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
    
    plt.title('Iraq_war risk', fontdict = font1)
    plt.savefig('Iraq_war_risk.png')
    plt.show()
    plt.close()

# kde
def plot_Iraq_war_KDE():
    retscomp = dfcom_Iraq_war.pct_change()
    corr = retscomp.corr()
    plt.imshow(corr, cmap='hot', interpolation='none')
    plt.colorbar()
    plt.xticks(range(len(corr)), corr.columns)
    plt.yticks(range(len(corr)), corr.columns)
    plt.title('Iraq_war correlation kde', fontdict = font1)
    plt.savefig('Iraq_war_correlation kde.png')
    plt.show()
    plt.close()
 
 

def output_plot():
    plot_911()
    plot_Iraq_war()
    return_911()
    return_Iraq_war()
    plot_DIAQQQ_911()
    plot_DIAQQQ_Iraq_war()
    plot_911_risk()
    plot_Iraq_war_risk()
    plot_911_KDE()
    plot_Iraq_war_KDE()


output_plot()
