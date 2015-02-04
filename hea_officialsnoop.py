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

def scoresheet_links(soup):
	print len('<a href="http://www.collegehockeystats.net')
	sheets = soup.select('tr td a')
	sheets_links = [str(line)[9:-9] for line in sheets if str(line).startswith('<a href="http://www.collegehockeystats.net', 0, 42)]
	final_sheets_links = [sheet.replace('" target="_blank">', '') for sheet in sheets_links]
	return final_sheets_links



# Takes .soup as input and finds all the boxscore links to be searched. 
def get_boxscore_links(soup):

	boxes = soup.select('tr td a')
	# for line in boxes:
		# if str(line).startswith('<a href="/men/tboxes15.php', 0, 26): 
	# for link in boxes:
	# 	print link

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
		game_details = single_game_soup.table.td.tr('td')
		# game_details shows every entry on the gamesheet.
		# game_details2 = single_game_soup.select('div.chsboxtop b br ')
		# print len(game_details2), game_details2[0] , '\n\n\n\n'

		# game_details3 = single_game_soup.select('p > b')
		# print game_details3

		referee1 = game_details[7]
		referee2 = game_details[12]
		lines1 = game_details[17]
		lines2 = game_details[22]

		# print game_details
		# print lines1, lines2
		# print ""
		# print referees
		# print "THIS IS A NEW GAME!"
		

		# Just a little Elbow Grease to clean things up a bit here:

		# print single_game_soup.select('.chsscore') , '\n\n\n'


		final['refs'] =  [str(game_details[7]).replace('<td valign="top">' , '').replace('</td>' , '') , str(game_details[12]).replace('<td valign="top">' , '').replace('</td>' , '')]

		final['lines'] = [str(game_details[17]).replace('<td valign="top">' , '').replace('</td>' , '') , str(game_details[22]).replace('<td valign="top">' , '').replace('</td>' , '')] 

		final['runtime'] = str(game_details[20]).replace('<td valign="top">', '').replace('</td>', '' )

		# Still need to find this in the parser... 
		# final['score'] = game_details[1]
		# print final['score']


		# print final['refs']
		# print final['lines']
		# print final['runtime']

		game_output.append( [ final['refs'], final['lines'],  final['runtime']  ,final['score']] )
		
		count += 1

		# Change the if statement to limit or de-limit the snooping. 
		if count == 15:
			break
	# print game_output
	return game_output


# --------------------------------------------------------------------------

def add_to_csv(to_add):
	official_dict = {
		'Referees' : '',
		'Linesmen' : '',
		'Runtime' : '',
		'BLANK' : '',
 	}



	fopen = open('/home/robby/Desktop/hea/official_list.csv', 'a')

	fwriter = csv.DictWriter(fopen, fieldnames = ['Referees', 'Linesmen', 'Runtime', 'BLANK'] )
	
	fwriter.writeheader()
	
	# official_dict['Referees'] = [game[0] for game in to_add]
	# official_dict['Linesmen'] = [game[1] for game in to_add]
	# official_dict['Runtime'] = [game[2] for game in to_add]
	# official_dict['BLANK'] = [game[3] for game in to_add]


	# print official_dict
	for game in to_add:
		
		fwriter.writerow( str(game[0]), str(game[1]), str(game[2]), str(game,3) )

	# print official_dict['Referees']
		
	
	

	fopen.close()


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


# boxscore_links = get_boxscore_links(composite_soup)

boxscore_links = scoresheet_links(composite_soup)

# games has thre { [refs] , [lines] , [score] , [gametime] } format
games = snoop_sheets(boxscore_links)

print "games: " , games
add_to_csv(games)

refs_all = seaperater(games, 0)

lines_all = seaperater(games, 1)

# print len(refs_all)
# print refs_all ,"\n\n\n"

# print len(lines_all)
# print lines_all
# print refs_all

# c = Counter(refs_all)
# d = c.most_common(10)

# lin = Counter(lines_all)
# limp = lin.most_common(10)
# for l in limp:
# 	print l

# for x in d:
# 	print x