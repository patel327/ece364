#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2016-01-15 19:12:33 -0500 (Fri, 15 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Prelab01/sum.bash $
#$Revision: 85146 $

X=0
Y=0
while (( $# != 0 ))
do
	Y=$1
	((X=X+$1))
	shift
	#((Y=Y+1))
done
echo $X
exit 0
