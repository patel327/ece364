#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2016-02-22 05:22:28 -0500 (Mon, 22 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Prelab06/email_edit.py $
#$Revision: 88545 $

import os
import sys
import re

def change():
    if not len(sys.argv) == 2:
        print("Usage: email_edit.py <filename>")
        return
    with open(sys.argv[1], "r")as fname:
        lines= fname.readlines()
        for line in lines:
            if not re.search("ecn.purdue.edu", line):
                gg = re.sub("purdue.edu", "ecn.purdue.edu", line)
                #print(gg)
                gs = re.sub(r"(\d{1,3})\.(\d{2})", r"\1.\2/100" , gg)
                #print(gs.groups())
                print(gs)
            else:
                gs = re.sub(r"(\d{1,3})\.(\d{2})", r"\1.\2/100" , line)
                print(gs)


if __name__ == '__main__':
    change()
    #print(sys.version)