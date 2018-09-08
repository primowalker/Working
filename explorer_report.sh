# The explorer_report.sh script take a directory containing Sun Solaris explorer files
# and gathers machine information such as machine type, memory size, disk info, etc.
# It then writes this information out into text files in the directory where this script
# is run, one for each machine.


# Get the path to the explorer files
if [ -n "$1" ]; then
        var="$1"
    else
        echo
        echo "Usage: explorer_report.sh <path to explorer directory>"
        echo
        echo "Example - explorer_report.sh /opt/SUNWexplo/output/"
        exit
fi
	
while true; do
	echo "NOTE - Explorer files are in tar.gz format and must be extracted before running this script."
    read -p "Are you sure you want to continue?  y/n: " yn
    case $yn in
        [Yy]* ) echo; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

# Get the explorer folder names
dir=`ls $1 | grep -v gz`

# Get the information for each system and write it out to a report.
for i in $dir;do
	echo "#### SYSTEM TYPE: ####" >> $i.txt
	echo  >> $i.txt
	cat $1/$i/sysconfig/uname-a.out >> $i.txt
	echo  >> $i.txt
	echo "#### SYSTEM INFO: ####" >> $i.txt
	cat $1/$i/sysconfig/prtdiag-v.out >> $i.txt
	echo >> $i.txt
	echo "---------------------------------------------------------------------" >> $i.txt
	echo  >> $i.txt
	grep banner-name $1/$i/sysconfig/prtpicl-v.out | sed -e 's/^[ \t]*//' | cut -d" " -f2,3,4 >> $i.txt
	echo "---------------------------------------------------------------------" >> $i.txt
	echo >> $i.txt
	echo "#### DISK INFO: ####" >> $i.txt
	cat $1/$i/disks/diskinfo | grep -v AVAILABLE | sed -e 's/^[ \t]*//' >> $i.txt
	echo "---------------------------------------------------------------------" >> $i.txt
	echo >> $i.txt
	echo "#### MEMORY INFO: ####" >> $i.txt
	echo >> $i.txt
	#grep 'Memory size' $1/$i/sysconfig/prtconf-vD.out | sed -e 's/^[ \t]*//' >> $i.txt
	echo >> $i.txt
	grep Memory $1/$i/sysconfig/prtconf-vD.out >> $i.txt
	echo "---------------------------------------------------------------------" >> $i.txt
	echo >> $i.txt
	echo "#### PARTS INFO: ####" >> $i.txt
	echo >> $i.txt
	grep 'model' $1/$i/sysconfig/prtconf-vP.out | sed -e 's/^[ \t]*//' >> $i.txt
	echo "---------------------------------------------------------------------" >> $i.txt
	echo >> $i.txt
	echo "#### FRU LIST: ####" >> $i.txt
	echo >> $i.txt
	grep -A6 FRU $1/$i/sysconfig/prtpicl-v.out | sed -e 's/^[ \t]*//' >> $i.txt
	echo >> $i.txt
	echo "#### PLATFORM INFO: ####" >> $i.txt 
	cat $1/$i/sysconfig/isainfo.out >> $i.txt
	echo >> $i.txt
	echo "#### PROCESSOR INFO: ####" >> $i.txt
	cat $1/$i/sysconfig/psrinfo-v.out >> $i.txt;
done


