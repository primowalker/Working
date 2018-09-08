#!/usr/bin/python

import os
import datetime

path = "/Users/jameswalker/iCloud/Archive"
newstring = datetime.date.today().strftime("%B_%d_%Y")

for filename in os.listdir(path):
    filename_without_ext = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1]
    new_file_name = filename_without_ext+"-"+newstring
    new_file_name_with_ext = new_file_name+extension
    print(new_file_name_with_ext)
    os.rename(os.path.join(path,filename),os.path.join(path,new_file_name_with_ext))