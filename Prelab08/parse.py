#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2016-03-06 15:53:05 -0500 (Sun, 06 Mar 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Prelab08/parse.py $
#$Revision: 89417 $

import sys

if __name__ == '__main__':
    z = None
    try:
        with open(sys.argv[1], "r") as fname:
            pass
    except(IndexError) as e:
        print("Usage: parse.py [filename]")
        z = e
    except(PermissionError) as p:
        print(str(sys.argv[1]) + " is not readable file.")
        z = p
    if z:
        sys.exit()

    with open(sys.argv[1], "r") as fname: # is this the way to check file i/o coz if else statements are better
        for lines in fname.readlines():
            sumlist = []
            sums = 0.0
            avg = 0.0
            stuff = None
            for values in lines.split():
                try:
                    sumlist.append(float(values))
                except:
                    if stuff == None:
                        stuff = values
                    else:
                        stuff += " " + values
            try:
                avg = sum(sumlist)/len(sumlist)
                if stuff:
                    print("{0:06.3f}".format(round(avg, 3)) + " " + stuff)
                    #temp +=  ": {0:03d},".format(self.simulationNumber)
                else:
                    print("{0:06.3f}".format(round(avg, 3)))
            except(ZeroDivisionError):
                print(lines.strip())




