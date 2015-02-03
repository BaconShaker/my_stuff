#!/usr/bin/python

# This is going to snoop the HEA website and list all the officials and their game totals. 


from bs4 import BeautifulSoup
import csv 
import os.path
import urllib
import urllib2
import os
import tabulate
import re
import numpy


# Opens link and returns a .soup-ed object
def make_soup(link):
	handle = urllib2.urlopen(link)
	soup = BeautifulSoup(handle)
	return soup
	handle.close()

# --------------------------------------------------------------------------

# Takes .soup as input and finds all the boxscore links to be searched. 
def get_boxscore_links(soup):

	boxes = soup.select('tr td a')
	# for line in boxes:
	# 	if str(line).startswith('<a href="/men/boxes15.php', 0, 25): 
		

	box_links = [str(line)[9:-9] for line in boxes if str(line).startswith('<a href="/men/boxes15.php', 0, 25)]


	final_box_links = [str('www.hockeyeastonline.com' + box) for box in box_links]
	return final_box_links

# --------------------------------------------------------------------------

def snoop_sheet(link_to_box):
	# Takes a list of links in string form from get_boxscores


	pass
# --------------------------------------------------------------------------



composite_schedule = 'http://www.hockeyeastonline.com/men/schedule/index.php'
composite_soup = make_soup(composite_schedule)
boxscore_links = get_boxscore_links(composite_soup)


print boxscore_links






