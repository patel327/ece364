#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2016-02-17 11:22:54 -0500 (Wed, 17 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Lab05/scheduler.bash $
#$Revision: 88365 $
#
if (($# != 1))
then
	echo "Usage: scheduler.bash <input file>"
	exit 1
fi
if [[ ! -e $1 ]]
then
	echo "Error: $1 does not exist."
	exit 2
fi
if [[ ! -r $1 ]]
then
	echo "Error: $1 is not readable."
	exit 2
fi
if [[ -e "schedule.out" ]]
then
	echo "Error: schedule.out already exists."
	exit 3
fi
echo "	07:00 08:00 09:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00" > schedule.out
IFS=","
while read -a line
do
	#echo ${line[0]}
	name=$(echo ${line[0]} | cut -d " " -f1)
	echo -n $name >> schedule.out
	line[0]=$(echo ${line[0]} | cut -d " " -f2)
	
	for item in ${line[*]}
	do
		#if $item == "07:00"
		#then
		#	echo "Y" >> schedule.out
		#fi
		echo $item
	done
	echo >> schedule.out
	
done < $1
