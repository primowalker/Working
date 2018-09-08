#!/usr/bin/python

import platform
import pwd
import grp
import os
import commands
from itertools import islice
import sys

# Get basic system info
node = platform.node()
linux_dist = platform.linux_distribution()
arch = platform.architecture()
kernel = platform.release()

# Get disk info
df = commands.getoutput('df -hP')
fstab = commands.getoutput('cat /etc/fstab')
fdisk = commands.getoutput('fdisk -l | grep /dev/')

# Get LVM information
pvs = commands.getoutput('pvs')
vgs = commands.getoutput('vgs')
lvs = commands.getoutput('lvs')

# Get networking info
ifconfig = commands.getoutput('ifconfig')
ipaddr = commands.getoutput('ip addr show')
iproute = commands.getoutput('ip route')
ipneigh = commands.getoutput('ip neigh show')
ntpq = commands.getoutput('ntpq -p  2')

# Get running processes
def ps():
	ps = commands.getstatusoutput("ps -ef")
	for proc in ps:
		print (proc)

# Get CPU info
cpuinfo = commands.getoutput("cat /proc/cpuinfo | grep processor | wc -l")

# Get Memory info
def meminfo():
	mem_info = commands.getoutput("cat /proc/meminfo")
	lines = mem_info.splitlines()
	iterator = islice(lines, 2)
	for i in iterator:
		print (i)

# Print all the users and their login shells
def user():
	users = pwd.getpwall()
	for user in users:
		print('{0}:{1}:{2}:{3}'.format(user.pw_name, user.pw_uid, user.pw_gid, user.pw_shell))

#Print all the groups
def group():
	groups = grp.getgrall()
	for group in groups:
		print('{0}:{1}:{2}'.format(group.gr_name, group.gr_gid, group.gr_passwd))

# Get shadow file info
shadow = commands.getoutput('cat /etc/shadow')

# Get crontab information
crontabs = commands.getoutput('tail -n +1 -- /var/spool/cron/tabs/*')

# Uptime, reboots, system crashes
uptime = commands.getoutput('uptime')
reboots = commands.getoutput('last | head -10')
crashes = commands.getoutput('last | grep crash')

# Messages and dmesg issues
dmesg = commands.getoutput('dmesg | grep -Ei \'(err|warn|fail)\' | grep -Eiv \'(interrupt|override)\'')
messages = commands.getoutput('cat /var/log/messages | grep -Ei \'(err|warn|fail)\' | grep -Eiv \'(interrupt|override|vas|syslog)\'')
