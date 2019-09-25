# -*- coding:utf-8 -*-
# 
'''
时间序列柱状图：

where 条件过滤
groupby 分组
matplotlib 画图
'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import datetime as dt
import pandas as pd

df = pd.read_csv('./text_score.csv', header=0, index_col='id', low_memory=False)

df['score'] = df['score'].astype(np.float64)
df = df.where(df['score'] < 0)
info = df.groupby('date').agg({'score':'sum','opt_times':'count'}).reset_index()

fig = plt.figure()
ax2 = fig.add_subplot()
date2_1 = dt.datetime(2008,3,1)
date2_2 = dt.datetime(2008,8,30)
delta2 = dt.timedelta(days=1)
dates2 = mpl.dates.drange(date2_1, date2_2, delta2)
y2 = info


ax2.bar(list(dates2), y2['score']/y2['opt_times'],linestyle='--')

dateFmt = mpl.dates.DateFormatter('%Y-%m-%d')
ax2.xaxis.set_major_formatter(dateFmt)
 
daysLoc = mpl.dates.DayLocator(interval=10)
hoursLoc = mpl.dates.DayLocator(interval=1)
ax2.xaxis.set_major_locator(daysLoc)
ax2.xaxis.set_minor_locator(hoursLoc)
 
fig.autofmt_xdate(bottom=0.18)
fig.subplots_adjust(left=0.18)
 
plt.show()