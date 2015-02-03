#!/usr/bin/python


import csv
from collections import Counter
from tabulate import tabulate

official_list = "/Users/AsianCheddar/Desktop/ushl_scrape/official_list.csv"
csvfile = open(official_list)
crew_list = csv.reader(csvfile, dialect = 'excel', skipinitialspace = True)
master_list = []
# for crew in crew_list:
# 	master_list.append(crew[0])
# 	master_list.append(crew[1])
# 	master_list.append(crew[2])
# 	master_list.append(crew[3])
# 	master_list.append(crew[4])

# total = Counter(master_list)

# # print list(total.elements())
# common = [entry for entry in total.most_common(45)]
# rank = 1
# for guy in common:

# 	print guy[0], " is listed on a gamesheet: " , guy[1], "times.		# " , rank
# 	rank += 1
# print ""
# print common

# unique = [[guy[0], guy[1]] for guy in common]

# print ""
# print unique
# pretty = tabulate(unique, headers = [ 'Name' , 'Games worked'])
# print "\n" * 20
# print "Here is the Master List for both the USHL and the SPHL. \n"

# print pretty

# print master_list


total_ushl = [game for game in crew_list if crew_list[0] == 'USHL']

total_sphl = [game for game in master_list if master_list[0] == 'SPHL']


print "USHL: " , total_ushl
print "\n" *5
print "SPHL: " , total_sphl

csvfile.close()