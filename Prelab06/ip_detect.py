#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2016-02-22 05:22:28 -0500 (Mon, 22 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Prelab06/ip_detect.py $
#$Revision: 88545 $

import re
import string
import sys

def validity():
    if not len(sys.argv) == 2:
        print("Usage: ip_detect.py <filename>")
        return
    with open(sys.argv[1], "r") as fname:
        lines = fname.readlines()
        for line in lines:
            #print(line)
            if re.match(r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4]{1}[0-9]{1}:|[01]?[0-9][0-9]?:)", line):
                port = line.split(":") #port numbers can be evaluated however u want

                if (port[1].strip()).isdigit():
                    #rint(line)
                    #print((port[1].strip()).isdigit())
                    if not int((port[1]).strip()) < 32767:
                        print(line.strip() + " Invalid Port Number")
                    elif not int((port[1]).strip()) > 1:
                            print(line.strip() + " Invalid Port Number")
                    elif int((port[1]).strip()) < 1024:
                        print(line.strip() + " Valid (root privileges required)")
                    else:
                        print(line.strip() + " Valid")
                else:
                    print(line.strip() + " Invalid Port Number")
            else:
                print(line.strip() + " Invalid IP Address")


if __name__ == '__main__':
    #print(sys.version)
    validity()