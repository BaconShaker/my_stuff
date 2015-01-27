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

composite_schedule = "http://ushlstats.stats.pointstreak.com/leagueschedule.html?leagueid=49&seasonid=12983"

def sift_games(link):
	handle = urllib2.urlopen(link)
	soup = BeautifulSoup(handle)
	# print handle
	# print soup.prettify()
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


gamesheets2 = []
for sheet in gamesheets:
	sheet = sheet.replace( 'gamesheet_full', 'boxscore')
	gamesheets2.append(sheet)

print gamesheets2
for game in gamesheets2:
	print ""
	link = "http://ushlstats.stats.pointstreak.com/" + game
	print  link
	hand = urllib2.urlopen(link)
	soup2 = BeautifulSoup(hand)
	cleaned_up = soup2.select(".notes")
	for thing in cleaned_up:
		analyze = str(thing.find_all('br'))
		end = analyze.find( 'Scorekeeper')
		print analyze[0:end].replace('<br>' , '\n')
	hand.close()









