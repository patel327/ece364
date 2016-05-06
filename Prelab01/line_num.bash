#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2016-01-15 20:34:14 -0500 (Fri, 15 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Prelab01/line_num.bash $
#$Revision: 85155 $

if (($# != 1))
then
	echo "User should provide one argument"
	exit 1
fi
if [[ ! -r $1 ]]
then
	echo "Cannot read $1"
	exit 1
fi
X=1
while read line
do
	echo "$X:$line"
	((X++))
done < $1
exit 0
