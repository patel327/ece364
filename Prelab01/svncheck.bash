#! /bin/bash
#
#$Author: ee364e07 $
#$Date: 2016-01-17 21:16:43 -0500 (Sun, 17 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Prelab01/svncheck.bash $
#$Revision: 85407 $
#exec 1<file_list
while read line <&3;
do
	if [[ $(svn status $line | head -c 1 ) == "?" ]]
	then
		#echo "$line is under control"
		if [[ -e $line ]]
		then
		echo $?		
		if [[ ! -x $line ]]
		then
			#echo $?			
			read -p "Do you want to make $line executable (y/n):" check
			if [[ $check == "y" ]]
			then
				chmod +x $line
			fi
		fi
		svn add $line				
		fi
	else
		if [[ -e $line ]]
		then		
		if [[ ! -x $line ]]
		then
			echo $line
			svn propset svn:executable ON $line
		fi
		else
			echo "Error: $line appears to not exist here or in svn"		
		fi
	fi	
	#if [[ svn status $line ]]
	#then
	#echo $line 	
	#fi
done 3<file_list
svn commit
echo "Auto-committing code"
exit 0
