#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2016-02-22 05:22:28 -0500 (Mon, 22 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Prelab06/function_finder.py $
#$Revision: 88545 $

import sys
import re
import os

def finda():
    if not len(sys.argv) == 2:
        print("Usage: function_finder.py <filename>")
        return
    if not os.path.exists(sys.argv[1]):
        print("{} does not exist!".format(sys.argv[1]))
        return
    if not os.access(sys.argv[1], os.R_OK):
        print("{} is not readable!".format(sys.argv[1]))
        return
    with open(sys.argv[1], "r") as fname:
        lines = fname.readlines()
        for line in lines:
            if re.search("def +(?P<fn>[\w-]+) *\((?P<arg>.*)\)", line):
                expline = re.search(r"def +(?P<fn>[\w-]+) *\((?P<arg>[-\w=, ]*)\):", line)
                #print(line)
                print(expline.group("fn"))
                #print(expline.group("arg"))
                argno=1
                for arg in (expline.group("arg").split(",")):
                    print("Arg" + str(argno) + ": " + arg.strip())
                    argno+=1


if __name__ == '__main__':
    finda()
    #print(sys.version)