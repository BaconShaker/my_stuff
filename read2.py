#!/usr/bin/python


import csv
from collections import Counter
from tabulate import tabulate


# In this py we are going to open the file with all the game crews in it. 
# This file should be in CSV form with the league in the first slot and 
# "BLANK" listed in the last slot (index == 5) if the game was worked by a 3-Man crew



# The file is located at:

csvfile = '/Users/AsianCheddar/Desktop/ushl_scrape/official_list.csv'

# Open the file...
handle = open(csvfile)
list_of_crews = csv.DictReader(handle, dialect = 'excel', skipinitialspace = True)

# Gets all the crews from respective league into one list. 
master_crews = []

sphl_crews = []

ushl_crews = []

nahl_crews = []



for crew in list_of_crews:
	master_crews.append(crew)
	if crew['League'] == "SPHL":
		sphl_crews.append(crew)
	elif crew['League'] == "USHL":
		ushl_crews.append(crew)
	elif crew['League'] == 'NAHL':
		nahl_crews.append(crew)



class League:
	def __init__(self, name):
		self.name = name
		self.games = []

	def add_games(self, games):
		
		print 'These are all the crews listed in the boxscores in the ', self.name, ':\n'
		for game in games:
			self.games.append( [game['Slot 1'], game['Slot 2'], game['Slot 3'], game['Slot 4']])
			


	def list_games(self):
		display = []
		count = 1
		for game in self.games:
			display.append([count, game[0], game[1], game[2], game[3]])
			count += 1
		print tabulate(display, headers = ['#', 'Slot 1', 'Slot 2', 'Slot 3', 'Slot 4'])

	def count_games(self):
		count = []
		for game in self.games:
			for guy in game:
				count.append(guy)
		disp = Counter(count).most_common()
		print "\n\nThis is the game count for the officials in the ", self.name, ": \n\n"
		print tabulate(disp, headers = ['Name', 'Number of Games'])

class master:
	def __init__(self, all_games):
		self.all_games = all_games
		
		
	def name_lookup(self, search_for):
		lookup = []

		for game in self.all_games:

			# For some reason this returns only the headers... 
			people = [ guy for guy in game ]
			print people
		
		# c = Counter(lookup)
		# print search_for , " was found", c[search_for], "times. "
			
		print "There's no results, try again bro. "


ushl = League('USHL')
ushl.add_games(ushl_crews)
# ushl.list_games()




sphl = League('SPHL')
sphl.add_games(sphl_crews)
# sphl.list_games()

nahl = League("NAHL")
nahl.add_games(nahl_crews)

sphl.count_games()
ushl.count_games()
nahl.count_games()

# print master_crews
master = master(master_crews)
master.name_lookup("NAHL")

