#!/usr/bin/python

# This is a python script that opens the Akira website and gets all the pertinant information. 
# Or at least that's what I'm going to try to do. 


import urllib
import urllib2
from bs4 import BeautifulSoup


def open_link(link):
	handle = urllib2.urlopen(link)
	soup = BeautifulSoup(handle)

	return soup
	handle.close()


#---------------------------------------------------------------------

def links_all(soup):

	for link in soup.find_all('a'):
		print link.get('href')


#---------------------------------------------------------------------


all_clothing = 'http://www.shopakira.com/categories/Shop-Women/'

soup_akira = open_link(all_clothing)

links_all(soup_akira)
















