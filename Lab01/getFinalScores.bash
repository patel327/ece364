#! /bin/bash
#
#$Author$
#$Date$
#$HeadURL$
#$Revision$
#
if(($#!=1))
then
	echo 'Usage: ./getFinalScores.bash <filename>'
	exit 1
fi
if [[ ! -e $1 ]]
then
	echo "Error reading input file: $1"
	exit 2
fi
FILE=$(echo "$1" | cut -d "." -f1)
#echo $FILE
FILENAME=$(echo "${FILE}.out")
if [[ -e $FILENAME ]]
then
	ERROR=$(echo "$FILENAME" | cut -d "/" -f2)	
	echo "Output file $ERROR already exists."
	exit 3
fi
#echo $?
#echo $FILENAME
while read line
do
	NAME=$(echo "$line" | cut -d "," -f1)
	AS=$(echo "$line" | cut -d "," -f2)
	M1=$(echo "$line" | cut -d "," -f3)
	M2=$(echo "$line" | cut -d "," -f4)
	PROJ=$(echo "$line" | cut -d "," -f5)
	
	let FS=$AS*15/100+$M1*30/100+$M2*30/100+$PROJ*25/100	
		
	echo $NAME,$FS >> $FILENAME
done < $1
#
exit 0
