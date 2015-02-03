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

