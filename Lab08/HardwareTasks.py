#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2016-03-21 00:47:39 -0400 (Mon, 21 Mar 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Lab08/HardwareTasks.py $
#$Revision: 89735 $

import sys
import re


def idIsAcceptable(ver_id):
    if re.search(r"^(\w+)$", ver_id):
        return True
    return False

def processSingle(ver_assignment):
    if re.search(r"\.(?P<port>\w+)\((?P<pin>\w+)\)", ver_assignment):
        m = re.search(r"\.(?P<port>\w+)\((?P<pin>\w+)\)", ver_assignment)
        #print(m.groups())
        return(m.group("port"), m.group("pin"))
    else:
        raise ValueError(ver_assignment)

def processLine(ver_line):
    if re.search(r"^ *(?P<cname>\w+)[ ]+(?P<iname>\w+)[ ]+\( *(?P<portmap>(\.(?P<port>\w+)\((?P<pin>\w+)\),? *)+)[ ]*\)$", ver_line):
        m = re.search(r"^ *(?P<cname>\w+)[ ]+(?P<iname>\w+) +\( *(?P<portmap>(\.(?P<port>\w+)\((?P<pin>\w+)\),? *)+)[ ]*\)$", ver_line)
        #print(m.group("portmap"))
        if not idIsAcceptable(m.group("cname")):
            raise ValueError(m.group("cname"))
        if not idIsAcceptable(m.group("iname")):
            raise ValueError(m.group("iname"))
        for check in m.group("portmap").split(","):
            if not processSingle(check.strip()):
                raise ValueError(check.strip())
        list = []
        for check in m.group("portmap").split(","):
            list.append(processSingle(check.strip()))
        return m.group("cname"), m.group("iname"), tuple(list)
        #print(m.groups())
    else:
        raise ValueError(ver_line)

if __name__ == '__main__':
    print(sys.version)
    print(idIsAcceptable("U1"))
    print(idIsAcceptable("What?"))
    #processSingle(".D(Q)")
    print(processLine("DFFSR Q_int1_reg ( .D(serial_in), .CLK(clk), .R(1), .S(n5), .Q(Q_int1) )"))