from matplotlib import pyplot as plt
import pandas as pd


plt.style.use('fivethirtyeight')


data = pd.read_csv('likes_data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count,likes,c=ratio,edgecolor='black',linewidth=1,alpha=0.75)
cbar = plt.colorbar()
cbar.set_label('satisfaction')
plt.xscale('log')
plt.yscale('log')
plt.legend()

plt.title('Trending youtube videos')
plt.xlabel('Views count')
plt.ylabel('Likes count')

plt.tight_layout()

plt.show()