#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2016-03-07 17:11:14 -0500 (Mon, 07 Mar 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Prelab08/listmod.py $
#$Revision: 89497 $

import math

def find_median(list1, list2):
    biglist = sorted(list1 +list2)
    median = biglist[math.floor((len(biglist)-1)/2)]
    return biglist, median

if __name__ == '__main__':
    input1 = [ int(x) for x in input("Enter the first list of numbers:").split() ]
    input2 = [ int(x) for x in input("Enter the second list of numbers:").split() ]
    print("First List:", input1)
    print("Second List:", input2)
    big, med = find_median(input1, input2)
    print("Merged List:", big)
    print("Median:", med)

#not sure what is trying to be learnt here

"""
Enter the first list of numbers: -2 1 5
Enter the second list of numbers: -1 9 3
First list: [-2, 1, 5]
Second list: [-1, 9, 3]
Merged list: [-2, -1, 1, 3, 5, 9]
Median: 1
"""