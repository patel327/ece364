#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2016-01-24 20:18:58 -0500 (Sun, 24 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Prelab02/process_temps.bash $
#$Revision: 86642 $
#
if (($# != 1))
then
	echo "Usage: process_temps.bash <input file>"
	exit 1
fi
if [[ ! -r $1 ]]
then
	echo "Error: $1 is not a readable file."
	exit 2
fi
exec 3< $1
read header<&3 #get rid of first line 
while read line
do
	arrval=($line)
	arrsize=${#arrval[*]}
	N=1
	sumt=0
	while (($N != $arrsize))
	do
		((sumt=sumt+${arrval[N]}))
		((N++))
	done
	((avg=$sumt/($arrsize-1)))
	#echo $avg
	#echo $arrsize
	#echo $line
	echo "Average temperature for time ${arrval[0]} was $avg C."
done <&3
exit 0
