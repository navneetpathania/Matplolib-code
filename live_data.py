from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
from itertools import count
import random

plt.style.use('fivethirtyeight')

index = count()

def animation(i):
	data = pd.read_csv('live_data.csv')
	x  = data['x_value']
	y1 = data['Channel_1']
	y2 = data['Channel_2']
	plt.cla()
	plt.plot(x,y1,label='Channel_1')
	plt.plot(x,y2,label='Channel_2')
	plt.legend()
	plt.tight_layout()


ani = FuncAnimation(plt.gcf(),animation,interval=1000)
plt.tight_layout()
plt.show()