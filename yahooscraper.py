'''
Author Scott Phillpott
Date 5/12/2017

Plot FireEye and Baracuda using pandas and matplotlib

Pretty sweet!

'''

print("Get Rich Scott!")

import pandas as pd
import pandas.datareader as web


import datetime 
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

start = datetime.datetime(2013,1,1)
end = datetime.date.today()

df1 = web.DataReader("FEYE", "yahoo", start, end)
df2 = web.DataReader("CUDA", "yahoo", start, end)
df3 = web.DataReader("RTNB", "yahoo", start, end)
print(df1.tail())
print(df2.tail())
print(df3.tail())

df1['Adj Close'].plot(label='FEYE')
df2['Adj Close'].plot(label='CUDA')
df3['Adj Close'].plot(label='RTNB')


plt.show()

