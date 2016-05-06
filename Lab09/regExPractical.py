#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2016-03-23 11:18:11 -0400 (Wed, 23 Mar 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Lab09/regExPractical.py $
#$Revision: 89869 $

import sys
import re

def getAddress(sentence):
    m = re.search(r"[0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}[-:][0-9a-fA-F]{2}",sentence)
    if not m:
        return None
    return m.group(0)

def getElements(fullAddress):
    m = re.search(r"^https?://([0-9a-zA-Z\.]+)/([a-zA-Z0-9]+)/([a-zA-Z0-9]+)$", fullAddress)
    if not m:
        return None
    return m.group(1),m.group(2),m.group(3)


def getSwitches(commandline):
    m = re.findall(r"[\+\\]([a-z])\s+([\w/\:\.]+)", commandline)
    m = sorted(m, key=lambda student: student[0])
    return m

if __name__ == '__main__':
    print(sys.version)
    s = "The card was at 58-1c-0a-6e-39-4d, but it was removed."
    #print(getAddress(s))
    url = "https://www.paypal.com/Customer1Area/Pay2"
    #expectedValue = "www.paypal.com", "Customer1Area", "Pay2"
    #print(getElements(url))
    commandline = r"myScript.bash +v  \i 2   +p  /local/bin/somefolder"
    print(getSwitches(commandline))