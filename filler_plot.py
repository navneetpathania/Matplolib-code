from matplotlib import pyplot as plt
import pandas as pd
import csv

plt.style.use('fivethirtyeight')


# with open('developers.csv','r') as csvfile:
# 	csv_reader = csv.DictReader(csvfile)
# 	for x in csv_reader:
# 		ages.append(x['Age'])
# 		alldev_sy.append(x['All_Devs'])
# 		py_sy.append(x['Python'])
# 		java_sy.append(x['JavaScript'])
data = pd.read_csv('developers.csv')
ages = data['Age']
all_devs = data['All_Devs']
py_sy = data['Python']


plt.plot(ages, py_sy, label='Python')
# plt.plot(ages, java_sy, label='JavaScript')

plt.plot(ages, all_devs, color='#444444',
         linestyle='--', label='All Devs')
overall_median =  57287
plt.fill_between(ages,py_sy,all_devs,where=(py_sy > all_devs),interpolate=True,alpha=0.25,label='Above Avg')
plt.fill_between(ages,py_sy,all_devs,where=(py_sy <= all_devs),interpolate=True,alpha=0.25,label='Below Avg')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()