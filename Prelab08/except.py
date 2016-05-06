#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2016-03-06 15:53:05 -0500 (Sun, 06 Mar 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Prelab08/except.py $
#$Revision: 89417 $

if __name__ == '__main__':
    values = input("Please enter some values:")
    vlist = []
    for value in values.split():
        try:
            vlist.append(float(value))
        except (ValueError):
            #print(value)
            pass
    print("The sum is:", sum(vlist))

"""
Please enter some values: -1 3 4.3 5 asdf 8 bbb 9 boilerup 1 fun ufn
The sum is: 29.3
"""