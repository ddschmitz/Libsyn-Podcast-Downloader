# Libsyn-Podcast-Downloader

## Download from Website.

Simple python program to download all of the podcasts on a specified Libsyn page.  Format for supplying a webpage to download from should look like this `http://billburr.libsyn.com/webpage/page/1/size/1000` where 1 is how many pages and 1000 is how many items appear per page.  Using this format will put all the podcasts on one long page which the program will then parse.  

#### Running.

######Linux

Requires [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)

`apt-get install python-bs4`

`python downloader.py`

######Windows

Just run windownloader.exe (source code for the .exe is `windownloader.py` and was made using [pyinstaller](http://www.pyinstaller.org/)). 
