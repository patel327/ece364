#! /bin/bash
#
#$Author$
#$Date$
#$HeadURL$
#$Revision$
#
if(($#!=1))
then
	echo 'Usage: ./getCourseStats.bash <course name>'
	exit 1
fi
if [[ $1 != "ece364" &&  $1 != "ece337" && $1 != "ece468" ]]
then
	echo "Error: course $1 is not a valid option."
	exit 5
fi
N=1
total=0
FILENAME=$(echo "gradebooks/${1}_section${N}.txt")
#echo $FILENAME
while [[ -e $FILENAME ]]
	do	
	#getFinalScores.bash 
	FILENAME=$(echo "gradebooks/${1}_section${N}.txt")
	if [[ -e $FILENAME ]]
	then	
		#echo $FILENAME
		getFinalScores.bash $FILENAME
		if(($?!=0))
		then
			echo "Error while running getFinalScores.bash"
			exit 3
		fi
		#let $total=$(wc -l $FILENAME)+$total
	fi	
	((N++))
		
	done
#
echo $total
exit 0
