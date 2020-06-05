#!/usr/bin/env python

from __future__ import print_function
import calendar
import argparse
import csv
import os

# Create the CLI parser
parser = argparse.ArgumentParser(description='',
    formatter_class=argparse.RawTextHelpFormatter,
    epilog = '')

# Get the input
parser.add_argument('year_in', help='The year you want')
parser.add_argument('month_in', help='The month you want')

# Initialize the parser
args = parser.parse_args()

# Set the year and month variables
year = int(args.year_in)
month = int(args.month_in)

# Print the calendar
print(calendar.month(year, month))
