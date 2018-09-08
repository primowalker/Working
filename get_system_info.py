#!/usr/bin/python

import sysinfo

# Get basic system info
nodename = sysinfo.node()
linuxdistro = sysinfo.linux_dist()
arch = sysinfo.arch()
kernel = sysinfo.kernel()
cpu_info = sysinfo.cpuinfo()
mem_info = sysinfo.meminfo()

# Get disk info
# Getting output of df -hP
df = sysinfo.df()
lines = df.splitlines()
print('Filesystem\tSize\tUsed\tAvail\tUsed%\tMounted on')
for line in lines[1:]:
	columns = line.split()
	filesystem = columns[0]
	size = columns[1]
	used = columns[2]
	available = columns[3]
	used_percentage = columns[4]
	mounted_on = columns[5]
	print (filesystem, '\t', size, used, '\t',  available, '\t',  used_percentage, '\t',  mounted_on)

fstab = sysinfo.fstab()
fdisk = sysinfo.fdisk()

# Get LVM info
physical_volumes = sysinfo.pvs()
volume_groups = sysinfo.vgs()
logical_volumes = sysinfo.lvs()

# Networking info
ifconfig = sysinfo.ifconfig()
ipaddr = sysinfo.ipaddr()
iproute = sysinfo.iproute()
ip_neigh = sysinfo.ipneigh()
ntp_info = sysinfo.ntpq()

# User and group info
users = sysinfo.user()
groups = sysinfo.group()
shadow_info = sysinfo.shadow()

# Running system processes
procs = sysinfo.ps()

# Crontab info
crontabs = sysinfo.crontabs()

# System uptime, reboots and crashes
uptime = sysinfo.uptime()
reboots = sysinfo.reboots()
crashes = sysinfo.crashes()

# Errors, warnings and failures
dmesg_errs = sysinfo.dmesg()
messages_errs = sysinfo.messages()
