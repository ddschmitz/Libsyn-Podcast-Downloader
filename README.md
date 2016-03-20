# Libsyn-Podcast-Downloader

Simple python program to download all of the podcasts on a specified Libsyn page.  Format for supplying a webpage to download from should look like this `http://billburr.libsyn.com/webpage/page/1/size/1000` where 1 is how many pages and 1000 is how many items appear per page.  Using this format will put all the podcasts on one long page which the program will then parse.  

### Setup

`./install-dependencies.sh`

### Running.

`python downloader.py`

### If You Encounter Troubles.

If you have any issues with downloads stopping, try using [torsocks](https://github.com/dgoulet/torsocks).

`torsocks python downloader.py`
