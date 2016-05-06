#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2016-01-25 17:06:44 -0500 (Mon, 25 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Prelab02/run.bash $
#$Revision: 86768 $
#
if (($# != 2))
then
	echo "Usage: yards.bash <filename source> <output file name>"
	exit 1
fi
gcc $1 -o quick_sim
if (($?))
then
	echo "$1 did not compile"
	exit 1
fi
if [[ -e $2 ]]
then
	read -p "$2 exists. Would you like to delete it? " answ
	if [[ $answ == "yes" || $answ == "y" ]]
	then
		rm $2
		#echo shubhamsux
		read -p "Enter a new filename: " newname
		touch $newname
		filen=$newname
	else
		filen=$2
	fi
else
	touch $2
	filen=$2	
fi
least=100000
for cs in 1 2 4 8 16 32
do
	for iw in 1 2 4 8 16
	do
		for pc in a i
		do
			pname=$(quick_sim $cs $iw $pc | cut -d ":" -f2)
			csize=$(quick_sim $cs $iw $pc | cut -d ":" -f4)
			iwidth=$(quick_sim $cs $iw $pc | cut -d ":" -f6)
			cpi=$(quick_sim $cs $iw $pc | cut -d ":" -f8)			
			time=$(quick_sim $cs $iw $pc | cut -d ":" -f10)
			echo "$pname:$csize:$iwidth:$cpi:$time" >> $filen
			if(($least>$time))
			then
				leastp=$pname
				leastc=$csize
				leasti=$iwidth
				leastcpi=$cpi
				leastt=$time
				least=$time
			fi
		done	
	done
done
echo "Fastest run time achieved by $leastp with $leastc and issue width $leasti was $leastt"
exit 0
