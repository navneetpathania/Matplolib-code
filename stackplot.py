from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

day = [1,2,3,4,5,6,7]
india = [100,110,300,350,444,498,600]
italy = [50,150,333,400,434,500,700]
america = [200,300,500,600,650,700,900]
labels = ['india','italy','america']

plt.stackplot(day,india,italy,america,labels=labels)
plt.legend(loc='upper left')
plt.title('Covid case in first 8 days')
plt.tight_layout()
plt.show()