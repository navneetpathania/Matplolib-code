from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
plt.style.use('fivethirtyeight')

with open('data.csv','r') as csvfile:
	csvreader = csv.DictReader(csvfile)
	language_counter = Counter()
	for item in csvreader:
		language_counter.update(item['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for row in language_counter.most_common(15):
	languages.append(row[0])
	popularity.append(row[1])
	print(row)
print(languages)
print(popularity)

languages.reverse()
popularity.reverse()
plt.barh(languages,popularity)


plt.title('Popular Languages')
# plt.ylabel('Language')
plt.xlabel("popularity")

# plt.legend()
# plt.xticks(languages,languages,size=6)
plt.tight_layout()

plt.show()