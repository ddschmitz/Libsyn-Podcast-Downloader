#   Author: Darrin Schmitz
#   Date: 3/19/2016


import urllib
import os
import re
import sys

pageInput = raw_input('\n\n\nPage you wish to download from: ')
DLlocation = raw_input('Download Location (Example: /home/Jon/Podcasts/):  ')

if not (os.path.exists(DLlocation)): #Check for valid download location
    sys.exit("%s is not a valid path." % DLlocation)

#Turn webpage into a parasable string.
page = urllib.urlopen(pageInput).read()

findEnclosure = re.compile('<enclosure.*')
findMp3 = re.compile('http.*.mp3')

for enclosure in findEnclosure.findall(page): #Find all enclosure tags on the page.
    for mp3 in findMp3.findall(enclosure): #Find the .mp3's in the enclosure tags.
        
        #Create path variable using user specified location and filename of .mp3.
        path = DLlocation + mp3.split('/')[-1] #split gets the .mp3 filename out of the url.

        if (os.path.exists(path)):
            print "%s already exists. Skipping to next one." % path
        else:
            print "Currently downloading %s" % mp3.split('/')[-1]
            urllib.urlretrieve(mp3, path)


#Format Output
for i in range(0, 10):
	print "\n"
print "\tAll of the MMPodcasts posted to billburr.libsyn.com should be downloaded."
print "\tRunning this script again will download any new podcasts and skip over"
print "\tones you already have.\n\n"
