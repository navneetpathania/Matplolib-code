from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

users = [2623, 2447, 2045, 1650, 1563]
languages = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0.1,0,0.1,0]

plt.pie(users,labels=languages,wedgeprops={'edgecolor':'black'},autopct='%1.1f%%',shadow=True,explode=explode,startangle=90)
plt.title('User of programing languages')
plt.tight_layout()
plt.show()