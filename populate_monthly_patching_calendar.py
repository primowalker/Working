#!/cygdrive/c/Users/f8tg2la/AppData/Local/Programs/Python/Python38

'''
    This script is meant to read in data from the Master_Linux_FDE_Patching_Schedule.csv file
    and generate a monthly patching schedule based on the days of month each server is required
    to be patched.

    We need to calculate the following days for each month of the year:
    2nd Monday
    3rd Monday
    4th Monday
    2nd Tuesday
    3rd Tuesday
    4th Tuesday
    2nd Wednesday
    3rd Wednesday
    4th Wednesday
    2nd Thursday
    3rd Thursday
    4th Thursday
    2nd Friday
    3rd Friday
    4th Friday
    3rd Saturday
    3rd Sunday
    Last Thursday of month
    End of month
    First day of next month

    Servers that have no specific day of month need to be randomly sorted into the 2nd, 3rd or 4th
    week for that specific day. For example, if 12 servers need to be patched on a Monday, but no
    specific week is required then they will be randomly sorted so that there are 4 servers in the
    3nd week, 4 in the 3rd week and 4 in the 4th week.

    A patching schedule for the specified month will then need to be written based on the above criteria.

    The script takes 2 arguments: year, month
'''
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

# Get our dates
c = calendar.Calendar(firstweekday=calendar.SUNDAY)

# Set the output file name
mon = str(month)
yr = str(year)
outfile = ('Linux_FDE_Patching_Schedule_' + mon + '_' + yr + '.csv')

# If the output file already exists, remove it
try:
    os.remove(outfile)
except:
    pass

# Open the file for writing
f = open(outfile, "a")

# Print the header to the output file
header = 'Server,OS Name,ENV,Virtual,Implementation Date,Day of week,Start Time,End Time,Time Zone,Old Kernel Release,New Kernel,Release,Special Instructions on reboot,Implementor,Status'
f.write(''.join(str(item) for item in header) + '\n')

# Get data from Master_Linux_FDE_Patching_Schedule.csv
with open('Master_Linux_FDE_Patching_Schedule.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        server = row[0]
        os = row[1]
        env = row[2]
        vm = row[3]
        day_of_month = row[4]
        start_time = row[5]
        end_time = row[6]
        time_zone = row[7]
        notes = row[8]

        # Get Mondays
        if day_of_month == '2nd Monday':
            monthcal = c.monthdatescalendar(year,month)
            secomd_monday = [day for week in monthcal for day in week if day.weekday() == calendar.MONDAY and day.month == month][1]
            output = (server, ',', os, ',', env, ',', vm, ',', secomd_monday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        if day_of_month == '3rd Monday':
            monthcal = c.monthdatescalendar(year,month)
            third_monday = [day for week in monthcal for day in week if day.weekday() == calendar.MONDAY and day.month == month][2]
            output = (server, ',', os, ',', env, ',', vm, ',', third_monday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        if day_of_month == '4th Monday':
            monthcal = c.monthdatescalendar(year,month)
            forth_monday = [day for week in monthcal for day in week if day.weekday() == calendar.MONDAY and day.month == month][3]
            output = (server, ',', os, ',', env, ',', vm, ',', forth_monday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        # Get Tuesdays
        if day_of_month == '2nd Tuesday':
            monthcal = c.monthdatescalendar(year,month)
            secomd_tuesday = [day for week in monthcal for day in week if day.weekday() == calendar.TUESDAY and day.month == month][1]

            output = (server, ',', os, ',', env, ',', vm, ',', secomd_tuesday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        if day_of_month == '3rd Tuesday':
            monthcal = c.monthdatescalendar(year,month)
            third_tuesday = [day for week in monthcal for day in week if day.weekday() == calendar.TUESDAY and day.month == month][2]
            output = (server, ',', os, ',', env, ',', vm, ',', third_tuesday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        if day_of_month == '4th Tuesday':
            monthcal = c.monthdatescalendar(year,month)
            forth_tuesday = [day for week in monthcal for day in week if day.weekday() == calendar.TUESDAY and day.month == month][3]
            output = (server, ',', os, ',', env, ',', vm, ',', forth_tuesday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        # Get Wednesdays
        if day_of_month == '2nd Wednesday':
            monthcal = c.monthdatescalendar(year, month)
            second_wednesday = [day for week in monthcal for day in week if day.weekday() == calendar.WEDNESDAY and day.month == month][1]
            output = (server, ',', os, ',', env, ',', vm, ',', second_wednesday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        if day_of_month == '3rd Wednesday':
            monthcal = c.monthdatescalendar(year, month)
            third_wednesday = [day for week in monthcal for day in week if day.weekday() == calendar.WEDNESDAY and day.month == month][2]
            output = (server, ',', os, ',', env, ',', vm, ',', third_wednesday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        if day_of_month == '4th Wednesday':
            monthcal = c.monthdatescalendar(year, month)
            forth_wednesday = [day for week in monthcal for day in week if day.weekday() == calendar.WEDNESDAY and day.month == month][3]
            output = (server, ',', os, ',', env, ',', vm, ',', forth_wednesday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        # Get Thursdays
        if day_of_month == '2nd Thursday':
            monthcal = c.monthdatescalendar(year,month)
            second_thursday = [day for week in monthcal for day in week if day.weekday() == calendar.THURSDAY and day.month == month][1]
            output = (server, ',', os, ',', env, ',', vm, ',', second_thursday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        if day_of_month == '3rd Thursday':
            monthcal = c.monthdatescalendar(year,month)
            third_thursday = [day for week in monthcal for day in week if day.weekday() == calendar.THURSDAY and day.month == month][2]
            output = (server, ',', os, ',', env, ',', vm, ',', third_thursday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        if day_of_month == '4th Thursday':
            monthcal = c.monthdatescalendar(year, month)
            forth_thursday = [day for week in monthcal for day in week if day.weekday() == calendar.THURSDAY and day.month == month][3]
            output = (server, ',', os, ',', env, ',', vm, ',', forth_thursday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        # Get Fridays
        if day_of_month == '2nd Friday':
            monthcal = c.monthdatescalendar(year,month)
            second_friday = [day for week in monthcal for day in week if day.weekday() == calendar.FRIDAY and day.month == month][1]
            output = (server, ',', os, ',', env, ',', vm, ',', second_friday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        if day_of_month == '3rd Friday':
            monthcal = c.monthdatescalendar(year,month)
            third_friday = [day for week in monthcal for day in week if day.weekday() == calendar.FRIDAY and day.month == month][2]
            output = (server, ',', os, ',', env, ',', vm, ',', third_friday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        if day_of_month == '4th Friday':
            monthcal = c.monthdatescalendar(year, month)
            forth_friday = [day for week in monthcal for day in week if day.weekday() == calendar.FRIDAY and day.month == month][3]
            output = (server, ',', os, ',', env, ',', vm, ',', forth_friday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        # Get Saturdays
        if day_of_month == '3rd Saturday':
            monthcal = c.monthdatescalendar(year, month)
            third_saturday = [day for week in monthcal for day in week if day.weekday() == calendar.SATURDAY and day.month == month][2]
            output = (server, ',', os, ',', env, ',', vm, ',', third_saturday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        # Get Sundays
        if day_of_month == '3rd Sunday':
            monthcal = c.monthdatescalendar(year, month)
            third_sunday = [day for week in monthcal for day in week if day.weekday() == calendar.SUNDAY and day.month == month][2]
            output = (server, ',', os, ',', env, ',', vm, ',', third_sunday, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')

        # Get data for last day of month
        if day_of_month == 'End of month':
            yr = str(year)
            mon = str(month)
            ldom = (calendar.monthrange(year, month)[1])
            last_of_month = str(ldom)
            last_day_of_month = (yr + '-' + mon + '-' + last_of_month)
            output = (server, ',', os, ',', env, ',', vm, ',', last_day_of_month, ',', day_of_month, ',', start_time, ',', end_time, ',', time_zone, ',', notes)
            f.write(''.join(str(item) for item in output) + '\n')
f.close()
