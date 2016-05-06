#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2016-01-24 17:19:47 -0500 (Sun, 24 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Prelab02/yards.bash $
#$Revision: 86605 $
#
if (($# != 1))
then
	echo "Usage: yards.bash <filename>"
	exit 1
fi
if [[ ! -r $1 ]]
then
	echo "Error: Cannot read $1"
	exit 1
fi
if [[ ! -e $1 ]]
then
	echo "$1 does not exist"
	exit 1
fi
greatest=0
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
		
	if(($avg>$greatest))
	then
		greatest=$avg
	fi
	var_sum=0
	N=1
	while (($N != $arrsize))
	do
		((var_sum=var_sum+(${arrval[N]}-avg)*(${arrval[N]}-avg)))
		((N++))
	done
	((var=$var_sum/($arrsize-1)))
	#echo $var
	echo "${arrval[0]} averaged $avg yards receiving with a variance of $var"
done < $1
echo "The largest average yardage was $greatest"
exit 0
