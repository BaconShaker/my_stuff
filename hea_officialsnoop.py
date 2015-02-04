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
from collections import Counter

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


	final_box_links = [str('http://www.hockeyeastonline.com' + box) for box in box_links]
	return final_box_links

# --------------------------------------------------------------------------

def snoop_sheets(links_to_boxes):
	# Takes a list of links in string form from get_boxscores
	# RETURNS a list containing [ ref, ref, line, line, Home/Away ]
	count = 0
	final = {
		'refs' : "",
		'lines' : "",
		'score' : "",
		'runtime' : "" ,
	}

	game_output = []
	


	for link in links_to_boxes:
		# print link
		single_game_soup = make_soup(link)
		game_details = single_game_soup.select('p b')
		# game_details shows every entry on the gamesheet.

		# Just a little Elbow Grease to clean things up a bit here:

		print single_game_soup.select('.chsscore') , '\n\n\n'


		final['refs'] =  str(game_details[1]).replace('<b>' , '').replace('</b>' , '').split(',')
		final['lines'] = str(game_details[2]).replace('<b>' , '').replace('</b>' , '').split(',')
		final['score'] = str(game_details[0]).replace('<b>' , '').replace('</b>' , '')
		final['runtime'] = str(game_details[6]).replace('<b>' , '').replace('</b>' , '')

		
		
		game_output.append( [ final['refs'], final['lines'], final['score'],  final['runtime']  ] )
		
		count += 1

		# Change the if statement to limit or de-limit the snooping. 
		if count == 15:
			break

	return game_output


# --------------------------------------------------------------------------

def seaperater(games, selector):
	output = [] 
	for game in games:
		output.append(game[selector][0])
		output.append(game[selector][1])

	return output

# --------------------------------------------------------------------------



# This is the link to the HEA main composite schedule
composite_schedule = 'http://www.hockeyeastonline.com/men/schedule/index.php'

# This opens the schedule link and makes a BeautifulSoup object to manipulate the HTML
composite_soup = make_soup(composite_schedule)

# This guy searches the soup we made above for all the links with box scores in them
# it returns a list of strings ready to be loaded into a bulk urlopener. 
boxscore_links = get_boxscore_links(composite_soup)


# print boxscore_links

# games has thre { [refs] , [lines] , [score] , [gametime] } format
games = snoop_sheets(boxscore_links)

refs_all = seaperater(games, 0)

# lines_all = seaperater(games, 1)

# print len(refs_all)
# print refs_all ,"\n\n\n"

# print len(lines_all)
# print lines_all
print refs_all

c = Counter(refs_all)
d = c.most_common(10)
for x in d:
	print x