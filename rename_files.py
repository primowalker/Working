#!/usr/bin/python

# Author: James Walker
# Version: 2.0
# Date: May 27, 2007

''' The rename_file.py scripts take the full path to the directory
	where your files to be renamed live.
	
	The newstring variable or "new identifier" is a string to add 
	onto the end of the file name when renaming it.
	
	For example if you have two files in /home/myhome/docs 
	named one.txt and index.html, and you want to rename them so they 
	become one-backup.txt and index-backup.html then you would run 
	the script like this:
	
	./rename_files.py 
	Enter the directory path where you need to rename
	Example "/home/myid/temp". Make sure to include the qoutes!
	: "/home/myhome/documents"
	Enter the new identifier to add to the file name
	Example  "-new",  "-1 ". Make sure to include the qoutes!
	: "-backup"
	
'''

import os

path = raw_input('Enter the directory path where you need to rename\nExample "/home/myid/temp"\n: ')
newstring = raw_input('Enter the new identifier to add to the file name\nExample  "-new",  "-1 "\n: ' )

for filename in os.listdir(path):
    filename_without_ext = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1]
    new_file_name = filename_without_ext+newstring
    new_file_name_with_ext = new_file_name+extension
    print(new_file_name_with_ext)
    os.rename(os.path.join(path,filename),os.path.join(path,new_file_name_with_ext))