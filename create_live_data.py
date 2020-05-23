import random
import time
import csv

index = 0
Channel_1 = 100
Channel_2 = 100
fieldnames = ['x_value',"Channel_1","Channel_2"]

with open('live_data.csv','w') as csv_file:
	csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
	csv_writer.writeheader()

while True:
	with open("live_data.csv",'a') as csv_file:
		csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		info = {
		'x_value':index,
		'Channel_1': Channel_1,
		'Channel_2': Channel_2
		}
		csv_writer.writerow(info)
		print(index,Channel_1,Channel_2)
		index += 1
		Channel_1 = Channel_1 + random.randint(-5,9)
		Channel_2 = Channel_2 + random.randint(-4,7)
		
	time.sleep(1)