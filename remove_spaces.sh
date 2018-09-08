#!/bin/sh
# this shell script removes the spaces out of the name of every file argument
# passed to it (handles an arbitrary number of files on the command line).
# example:
# sqzspaces.sh "/Users/Kurt/Name With Spaces"
# results in changing the filename to "/Users/Kurt/NameWithSpaces"

FileName=`find . -exec detox {} \;`
