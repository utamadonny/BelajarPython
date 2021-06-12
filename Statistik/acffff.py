# %%
import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
import matplotlib.pyplot as plt
from scipy import signal

# dsun=[]
# dtemp=[]
# for i in range(0,2000):
sun=pd.read_csv('daily-max-temperatures.csv',delimiter=",",header=0)
max_temp=pd.read_csv('monthly-sunspots.csv',delimiter=",",header=0)
#? Convert ke numpy array dan ambil 1000 data sampel
sun1=sun[["Temperature"]].loc[1:100].to_numpy() 
temp1=max_temp[["Sunspots"]].loc[1:100].to_numpy()
x, y = np.random.randn(2, 100)
#,header=0,index_col=0)
	# dsun.append(sun)
	# dtemp.append(max_temp)
# sun=np.asarray(dsun)
# max_temp=np.asarray(dtemp)

# %%
#! CCF using Numpy korelasi antara sunspot dengan temperatur maximal
ccorr = signal.correlate(sun1, temp1, mode='same') / 128
# cf1=np.correlate(sun,max_temp,mode='valid')


# %%
fig, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
ax1.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax1.grid(True)

ax2.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax2.grid(True)
# plot_acf(sun)
# plot_acf(max_temp)

plt.show()
# %%
