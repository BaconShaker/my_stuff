#!/usr/bin/python


import csv
from collections import Counter

official_list = "/Users/AsianCheddar/Desktop/ushl_scrape/official_list.csv"
csvfile = open(official_list)
crew_list = csv.reader(csvfile, dialect = 'excel')
master_list = []
for crew in crew_list:
	master_list.append(crew[0])
	master_list.append(crew[1])
	master_list.append(crew[2])
	master_list.append(crew[3])

total = Counter(master_list)

# print list(total.elements())
print total.most_common(25)


# all_positions = [[i[0] , i[1], i[2], i[3]] for i in crew_list]
# print Counter(all_positions)

# c =  Counter([x[0] for x in crew_list])

# a = Counter(pos1)
# print a

# print c.most_common(2)










# first_position = [position[0]for position in crew_list]
# second_position = [position[1] for position in crew_list]
# third_position = [position[2] for position in crew_list]
# fourth_position = [position[3] for position in crew_list]

# print first_position
# print Counter(first_position)
# print Counter(second_position)
# print Counter(third_position)
# print Counter(fourth_position)


# for x in first_position:
# 	print Counter(x)


# print cnt

csvfile.close()