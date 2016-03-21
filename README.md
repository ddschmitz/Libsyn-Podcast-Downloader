# Libsyn-Podcast-Downloader

Simple python program to download all of the podcasts on a specified Libsyn page.  Format for supplying a webpage to download from should look like this `http://billburr.libsyn.com/webpage/page/1/size/1000` where 1 is how many pages and 1000 is how many items appear per page.  Using this format will put all the podcasts on one long page which the program will then parse.  

## Setup

### Windows

1. Get the latest Python 2.7 release (currently 2.7.11) from https://www.python.org/downloads/
2. Run the installer, making sure to select "add python.exe to Path" in the installation options
3. Open an administrator command prompt in this folder, and run `python installer.py`

### Linux

Run `./linux-dependencies.sh`

## Running

Run `python downloader.py`
