#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2016-03-23 11:21:16 -0400 (Wed, 23 Mar 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Lab09/timeManager.py $
#$Revision: 89881 $

import sys

from timeDuration import *

def getTotalEventSpan(eventName):
    total = TimeSpan(0,0,0)
    with open("Events.txt") as fname:
        lines = fname.readlines()
        for line in lines[2:]:
            words = line.split()
            if words[0] == eventName and int(words[2]) > 0:
                if words[1][2] == "w":
                    total += (TimeSpan(int(words[1][0] + words[1][1]),0,0) * int(words[2]))

                if words[1][2] == "d":
                    total += (TimeSpan(0,int(words[1][0] + words[1][1]),0) * int(words[2]))
                if words[1][2] == "h":
                    total += (TimeSpan(0,0,int(words[1][0] + words[1][1])) * int(words[2]))
    str(total)
    return total

def rankEventsBySpan(*args):
    li = []
    for arg in args:
        li.append(arg)
    print(li)
    li = sorted(li, key = lambda student: TimeSpan.getTotalHours(getTotalEventSpan(student)), reverse= True)
    print(li)
    return li



if __name__ == '__main__':
    print(sys.version)
    getTotalEventSpan("Event13")
    rankEventsBySpan("Event00", "Event09", "Event17")