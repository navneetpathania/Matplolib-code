from matplotlib import pyplot as plt
import pandas as pd
import csv

plt.style.use('fivethirtyeight')


data = pd.read_csv('developers.csv')
ages = data['Age']
# all_devs = data['All_Devs']
# py_sy = data['Python']
bins = [10,20,30,40,50,60,70,80]

plt.hist(ages, bins=bins,edgecolor='black',log=False)
median_age = 29
plt.axvline(median_age,color='#fc4f3a',label='Age median')
# plt.plot(ages, java_sy, label='JavaScript')


plt.legend()

plt.title('Age of Respondent')
plt.xlabel('Ages')
plt.ylabel('Number of Respondent')

plt.tight_layout()

plt.show()