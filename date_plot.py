from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta
import pandas as pd

plt.style.use('seaborn')

dates = [
datetime(2015,5,26),
datetime(2015,5,27),
datetime(2015,5,28),
datetime(2015,5,29),
datetime(2015,5,30),
datetime(2015,5,31),
datetime(2015,6,1)
]
y = [1,2,3,5,4,6,7]
plt.plot_date(dates,y,linestyle='solid')
plt.gcf().autofmt_xdate()
dateformat = mpl_dates.DateFormatter('%b %d %y')
plt.gca().xaxis.set_major_formatter(dateformat)
plt.show()