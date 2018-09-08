#!/usr/bin/python

#Author: Suraj Patil
#Version: 1.0
#Date: 25th March 2014

# Modified by James Walker
# Version: 1.1
# Date: 8 May 2017

'''change filenames of all files in the given path to something you put there, You can name them in some order,
 like Photo001, Photo002 etc, of great help when you have a lot of files with contextual names'''
 
import os
from distutils.dir_util import copy_tree
import datetime
import glob

# Set the variables
path = "/Users/jameswalker/Pictures/Misc/"
new_file_name = datetime.date.today().strftime("%B_%d_%Y")
file_extension = "jpeg"

# Copy the files from iCloud to local drive
fromDirectory = "/Users/jameswalker/iCloud/Archive"
toDirectory = "/Users/jameswalker/Pictures/Misc"

copy_tree(fromDirectory, toDirectory)

# Fix the file extension
file_extension = (str('.')+ file_extension)

j=0
os.chdir(path)
for i in os.listdir(path):
	os.rename(i,new_file_name+ str(j)+file_extension)
	j+=1
	
# Remove the files from the iCloud directory
files = glob.glob('/Users/jameswalker/iCloud/Archive/*')
for f in files:
    os.remove(f)