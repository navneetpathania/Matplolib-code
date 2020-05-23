from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('seaborn')

data = pd.read_csv('developers.csv')
age = data['Age']
All_dev_sy = data['All_Devs']
py_sy = data['Python']
js_sy = data['JavaScript']
fig1, (col1,col2)= plt.subplots(nrows=2,ncols=2,sharex=True)
(ax1,ax2) = col1
print(ax1)
(ax3,ax4) = col2

ax1.plot(age,All_dev_sy,linestyle='--',label='All_Devs')
ax2.plot(age,py_sy,label='Python')
ax3.plot(age,js_sy,label='JavaScript',color='red')

ax1.legend()
ax1.set_title('Median salary(USD) with Ages')
ax1.set_ylabel("Median Salary")

ax2.set_xlabel('Ages')
ax2.set_ylabel("Median Salary")
ax2.legend()

plt.tight_layout()
fig1.savefig('subplot.png')
plt.show()
