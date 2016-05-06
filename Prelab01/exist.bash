#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2016-01-17 20:25:13 -0500 (Sun, 17 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Prelab01/exist.bash $
#$Revision: 85391 $
#
while(($# != 0))
do
	
	if [[ -r $1 ]]
	then
		echo "File $1 is readable!"
	elif [[ ! -e $1 ]]
	then
		touch $1
	fi
	shift
done
exit 0
