#!/bin/bash
#
#   Author: Darrin Schmitz, Ryan Rowe
#   Date: 3/21/2016
#
#   Uses code from http://stackoverflow.com/a/19520888/2508324

YUM_CMD=$(which yum)
APT_GET_CMD=$(which apt-get)

if [[ ! -z $YUM_CMD ]]; then
    sudo yum install python2.7
 elif [[ ! -z $APT_GET_CMD ]]; then
    sudo apt-get python2.7
else
	echo "error can't install python2.7 and python-bs4"
	exit 1;
fi

sudo python install.py
