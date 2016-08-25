from bs4 import BeautifulSoup
import urllib
import os
from random import randint
from time import sleep
import re
import sys
from Tkinter import *
import tkFileDialog
import threading

def saveLocation():
    global DLlocation
    DLlocation = tkFileDialog.askdirectory()
    DLlocation = DLlocation.replace('/', '\\') #Change forward slashes to back slashes since it's Windows.
    DLlocation = DLlocation + "\\"
    
    saveEntry.delete(0, END)
    if not (os.path.exists(DLlocation)): #Check for valid download location
        text.insert(END, "\n\n\"%s\" is NOT a valid path.  Please try again\n" % DLlocation)
        text.see(END)
        DLlocation = "INCORRECT"
        saveEntry.insert(0, DLlocation)
    elif (os.path.exists(DLlocation)):
        text.insert(END, "\n\n\"%s\" is a valid path.  Click \"Start\" to begin.\n\n\n" % DLlocation)
        text.see(END)
        saveEntry.insert(0, DLlocation)
    
    print ("Here ")
    print DLlocation

def startClick():
    #Since tkinter runs in a single thread, we have to put all the logic for
    #downloading the podcasts into another thread.  Otherwise the program would freeze
    #while the downloading was happening.
    def callback():
        global DLlocation
    
        pageInput = URLEntry.get()
        if (pageInput == ""):
            text.insert(END, "\n\nPlease choose a valid URL to download from.\n")
            text.see(END)
            return
            
        if (DLlocation == "INCORRECT"):
            text.insert(END, "\n\nPlease choose a valid save location.\n")
            text.see(END)
            return

        #Get page and use BeautifulSoup to make into a tree thing or something?
        print pageInput
        if (pageInput == "None"): #Sometimes pageInput is 'None', so keep trying.
            callback()
            return
        page = urllib.urlopen(pageInput).read()
        soup = BeautifulSoup(page, "lxml")

        #Find all the divs with the class postDetails.  This is the div that contains the download link.
        special_divs = soup.find_all('div', {'class' : 'postDetails'})
        for div in special_divs:

            #In each div find the anchor tag that has the .mp3 download link.
            download = div.find_all('a', href = re.compile('\.mp3$'))
            for anchor in download:
                hrefText = (anchor['href'])
                mp3Name = anchor.text #Used to see if we already downloaded this podcast.
                path = DLlocation + mp3Name
                        
                if (os.path.exists(path)): #os.path.exists() returns true if path refers to an existing path.
                    text.insert(END, "%s has already been downloaded. Skipping to next one.\n" % mp3Name)
                    text.see(END)
                else:
                    text.insert(END, "Currently downloading: %s\n" % hrefText)
                    text.see(END)
                    urllib.urlretrieve(hrefText, DLlocation + mp3Name)

        text.insert(END, "\n\n\n   All of the MMPodcasts posted to billburr.libsyn.com should be downloaded.\n")
        text.insert(END, "   Running this script again will download any new podcasts and skip over\n")
        text.insert(END, "   tones you already have.\n\n")
        text.see(END)
        
    t = threading.Thread(target=callback)
    t.start()

#Create widgits.
root = Tk()
root.wm_title("Libsyn Podcast Downloader")
div1 = Frame(height = 500, width = 500, bd = 2, relief = RIDGE)
div2 = Frame(height = 10, bd = 2, relief = RIDGE)
text = Text(div2)
startBtn = Button(div1, text = "Start", command = startClick)
saveBtn = Button(div1, text = "Save Location", command = saveLocation)
URLLabel = Label(div1, text = "                   URL:")
URLEntry = Entry(div1, width = 30)
saveEntry = Entry(div1, width = 30)

#Draw the widgets in the program's window.
div1.grid(row = 0, column = 0)
div2.grid(row = 0, column = 1)
URLLabel.grid(row = 0, column = 0, pady = 5)
URLEntry.grid(row = 0, column = 1)
saveBtn.grid(row = 1, column = 0, pady = 5, padx = 5)
saveEntry.grid(row = 1, column = 1)
startBtn.grid(row = 2, column = 0, pady = 5, padx = 5)
text.grid()

#Global variable for the download location.
DLlocation = ""

text.insert(END, "-----------------------INSTRUCTIONS-----------------------\n")
text.insert(END, "Paste a valid URL in the box to the left.\n")
text.insert(END, "Example URl: http://billburr.libsyn.com/webpage/page/1/size/10\n")
text.insert(END, "    The page size should be set to 1.\n")
text.insert(END, "    The size should be set to how many podcasts you want downloaded.\n")
text.insert(END, "\nClick \"Save Location\" to choose a location to save the podcasts to.\n")
text.insert(END, "\nClick \"Start\" when those are finished.\n")
text.insert(END, "----------------------------------------------------------\n")

root.mainloop()
