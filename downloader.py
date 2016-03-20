#   Author: Darrin Schmitz
#   Date: 3/19/2016


from bs4 import BeautifulSoup
import urllib
import os
from random import randint
from time import sleep
import re
import sys

pageInput = raw_input('\n\n\nPage you wish to download from: ')
DLlocation = raw_input('Download Location (Example: /home/Jon/Podcasts/):  ')

if not (os.path.exists(DLlocation)): #Check for valid download location
    sys.exit("%s is not a valid path." % DLlocation)

#Get page and use BeautifulSoup to make into a tree thing or something?
page = urllib.urlopen(pageInput).read()
soup = BeautifulSoup(page, "lxml")

#Find all the divs with the class postDetails.  This is the div that contains the download link.
special_divs = soup.find_all('div', {'class' : 'postDetails'})
for div in special_divs:

	#In each div find the anchor tag that has the .mp3 download link.
	download = div.find_all('a', href = re.compile('\.mp3$'))
	for anchor in download:
		hrefText = (anchor['href'])
		exists = anchor.text #Used to see if we already downloaded this podcast.
                path = DLlocation + exists
                
                if (os.path.exists(path)): #os.path.exists() returns true if path refers to an existing path.
			print "%s has already been downloaded. Skipping to next one." % exists

		else:
			print "Currently downloading: %s\n\n" % hrefText
			os.system('wget %s -P %s' % (hrefText, DLlocation)) #Download the .mp3 with wget.
		
			#Use this section if you think you are having issues downloading.
			#This code will make the script pause after every download for a random amount of time
			#between 60 and 180 seconds.  This may or may not help.
			#number = randint(60, 180)
			#print "Sleeping for %d seconds so we don't get blocked by the server." % number
			#sleep(number)

			#Format Output
			for i in range(0, 10):
				print "\n"
#Format Output
for i in range(0, 10):
	print "\n"
print "\tAll of the MMPodcasts posted to billburr.libsyn.com should be downloaded."
print "\tRunning this script again will download any new podcasts and skip over"
print "\tones you already have.\n\n"
