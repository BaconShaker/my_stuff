#!/usr/bin/python

# This is a Python script that is able to look up all the games in the 
# USHL and display who's working where. 

# Later, I would like to add the functionality of being able to interpret 
# referees' habits and predict team compatibility. Basically predict
# game difficulty from the Official's standpoint. 


from bs4 import BeautifulSoup
import csv 
import os.path
from datetime import datetime
import urllib
import urllib2
import os
import tabulate
import re
import numpy
from collecitons import counter

composite_schedule = "http://ushlstats.stats.pointstreak.com/leagueschedule.html?leagueid=49&seasonid=12983"

def sift_games(link):
	handle = urllib2.urlopen(link)
	soup = BeautifulSoup(handle)
	# print handle
	# print soup.prettify()
	# Make it so IF the date was too long ago it returns nothing. I only want tonight in this program. 



	contents = soup.find_all(target='_blank')
	
	prefix = '<a href="gamesheet_full.html?gameid='
	r = len(prefix)  
	print r 
	# This part will display only games that have already happened. 
	count = 1
	sheets = []
	for game in contents:
		# print game 
		game = str(game)
		if game.startswith('<a href="gamesheet_full.html', 0  ,  28):
			# print "This is game #" , count , ": ", game[9: r + 7] , '\n'
			count += 1
			sheets.append(game[9: r + 7])
	return sheets

	handle.close()

gamesheets = sift_games(composite_schedule)

print gamesheets
def show_box(gamesheets):
	boxscore = []
	game_number = 1
	gamesheets2 = []
	for sheet in gamesheets:
		sheet = sheet.replace( 'gamesheet_full', 'boxscore')
		gamesheets2.append(sheet)

	# print gamesheets2
	sike = 0
	# while sike == 0:
	for game in gamesheets2:
		print ""
		link = "http://ushlstats.stats.pointstreak.com/" + game
		# print  link
		hand = urllib2.urlopen(link)
		soup2 = BeautifulSoup(hand)
		cleaned_up = soup2.select(".notes")

		for thing in cleaned_up:
			analyze = str(thing.find_all('br'))
			end = analyze.find( 'Scorekeeper')
			final = analyze[1:end].replace('<br>' , ';')
			# print final 
			final2 = final.split(";")
			final3 = final2[1:-1]
		
		# print "This is game #" , game_number , final3
		game_number += 1

		boxscore.append(final3)

		hand.close()
			# if game_number == 6:
			# 	sike = 1
			# 	break
	return boxscore

ushl_scrape = show_box(gamesheets)
# Get rid of the blank spaces in the list...

# For DEBUGGUNG
for index, entry in enumerate(ushl_scrape):
	print "\nThis is game INDEX#:" ,  index + 1
	info = [i for i in entry]
	couple = (index , info)

	print couple




def seperate(boxscores):
	crop = boxscores
	counts = 0 
	how_long = len(boxscores)
	print "Boxscores is ", how_long, " things long."
	
	for game in boxscores:


		if counts <= how_long:
			crop[counts] = str(game[1:]).replace('Referee: ' , '')
			crop[counts] = str(crop[counts]).replace('Referee 2: ' , '')
			crop[counts] = str(crop[counts]).replace('Linesman 1: ' , '')
			crop[counts] = str(crop[counts]).replace('Linesman 2: ' , '')
			crop[counts] = str(crop[counts]).replace("'"  ,  " ")
			crop[counts] = str(crop[counts]).replace("[" , "")
			crop[counts] = str(crop[counts]).replace("]", "")
			guys = crop[counts].count(',') + 1
			if guys < 4:
				crop[counts] += ',  BLANK'

			print "\nThere were " , guys, " officials in game " , counts + 1 , ": \n"
			print crop[counts] , "\n"
		counts += 1

	print ""
	# print "This is crop: " , crop
	print ""
	return crop

officials = seperate(ushl_scrape)
print ""
print "This is officials: " , officials




def add_to_csv(crew):
	fopen = open('/Users/AsianCheddar/Desktop/ushl_scrape/official_list.csv', 'a')
	fwriter = csv.writer(fopen, quoting = csv.QUOTE_MINIMAL)
	print "This is crew: " , crew
	
	fwriter.writerow(crew)

	fopen.close()


for crew in officials:

	add_to_csv(crew.split(','))





