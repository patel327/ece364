#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2016-01-27 11:19:20 -0500 (Wed, 27 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Lab02/printUsageStats.bash $
#$Revision: 87088 $
#
if (($# != 1))
then
	echo "Usage: printUsageStats.bash <input file>"
	exit 1
fi
if [[ ! -e $1 ]]
then
	echo "Error: $1 does not exist."
	exit 2
fi
exec 4< $1
read header <&4
#echo $header | cut -f3
timestamp=$(echo $header | cut -d " " -f3)
echo "Parsing file "$1". Timestamp: $timestamp"
echo "Your choices are:"
echo "1) Active user IDs"
echo "2) N Highest CPU usages"
echo "3) N Highest mem usages"
echo "4) Top 3 longest runnning processes"
echo "5) All processes by a specific user"
echo "6) Exit"
echo
#
tail -n +8 $1 > forcpu.txt


while ((1))
do
	read -p "Please enter your choice: " choice
	if (($choice == 1))
	then
		userno=$(echo $header | cut -d " " -f8)
		echo "Total number of active user IDs: $userno"
	elif (($choice == 2))
	then
		read -p "Enter a Value for N: " Nval
		counter=0
		while read line
		do
			user=$(echo $line | cut -d " " -f2)
			cpu=$(echo $line | cut -d " " -f9)
			((counter++))
			echo "User $user is utilizing CPU resources at $cpu%"
			if((counter == Nval))
			then
				break
			fi
		done < forcpu.txt
	elif (($choice == 3))
	then
		sort -r -k10 forcpu.txt > formem.txt		
		read -p "Enter a Value for N: " Nval
		counter=0
		while read line
		do
			user=$(echo $line | cut -d " " -f2)
			mem=$(echo $line | cut -d " " -f10)
			((counter++))
			echo "User $user is utilizing mem resources at $mem%"
			if((counter == Nval))
			then
				break
			fi
		done < formem.txt
	elif (($choice == 4))
	then
		sort -r -n -k11,11 forcpu.txt > fortime.txt
		counter=0		
		while read line
		do
			pid=$(echo $line | cut -d " " -f1)
			command=$(echo $line | cut -d " " -f12)
			((counter++))
			echo "PID: $pid, cmd: $command"
			if((counter == 3))
			then
				break
			fi
		done < fortime.txt
	elif (($choice == 5))
	then
		read -p "Please enter a valid username: " user
		cat forcpu.txt | grep $user > user.txt
		if(($? != 0))
		then
			echo "No match found"
		else
			while read line
			do
				cpu=$(echo $line | cut -d " " -f9)
				command=$(echo $line | cut -d " " -f12)
				echo "$cpu $command"
			done < user.txt
		fi
			
	elif (($choice == 6))
	then
		exit 0
	fi
done

