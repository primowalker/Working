#/bin/bash
# "mp3 id3 tag to sql" importer by mutante
# reads id3 tags using "mp3info" and outputs a dumpfile that can be imported to mysql
# how to import outfile:
# mysql -u user -p songs < mp3.sql

# good ones to outfile
outfile="mp3.sql"

# errors to error file (files without id tag)
errfile="mp3.err"

# counter 
count=1

# adjust your path here
find /Users/jpwalker/OneDrive/Music/Music/ -name \*.mp3 -print | while read file

do

# writing to out-files (mp3info rocks, -p option is like a printf statement)

mp3info -p "insert into songs (filename,artist,title,album,comment,track,year,genre,path,filesize,copyright,layer,
stereo,goodframes,badframes,frequency,playtime) VALUES
(\"%f\",\"%a\",\"%t\",\"%l\",\"%c\",\"%n\",\"%y\",\"%g\",\"%F\",\"%k\",\"%C\",\"%L\",\"%o\",\"%u\",\"%b\",\"%Q\",\"%S\");" "$file" 1>>$outfile 2>>$errfile

# some additional,but unnecessary screen output,to see if the script is still running

echo -e "\n \n id: $count -"
mp3info -p "%a,%t,%F" "$file"

let "count+=1"

done

