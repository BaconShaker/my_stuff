#!/usr/bin/python

from collections import counter
import csv


official_list = "/Users/AsianCheddar/Desktop/ushl_scrape/official_list.csv"
csvfile = open(official_list)
crew_list = csv.reader(csvfile, dialect = 'excel')


for crew in crew_list:
	print crew





csvfile.close()