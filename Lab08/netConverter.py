#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2016-03-21 00:48:20 -0400 (Mon, 21 Mar 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Lab08/netConverter.py $
#$Revision: 89736 $

import sys
import HardwareTasks

def verilog2vhdl(ver_line):
    try:
        comp, inst, tuppin = HardwareTasks.processLine(ver_line)
    except:
        return "Error: Bad Line."

    vhdlstr = inst + ": " + comp + " PORT MAP("
    for item in tuppin[:-1]:
        vhdlstr += item[0] + "=>" + item[1] + ", "
    vhdlstr += tuppin[-1][0] + "=>" + tuppin[-1][1] + ");"
    return vhdlstr

def convertNetlist(sourceFile, targetFile):
    results = []
    with open(sourceFile, "r") as fname:
        lines = fname.readlines()
        for line in lines:
            results.append(verilog2vhdl(line) + "\n")
    results[-1] = results[-1].strip()
    with open(targetFile, "w") as fname:
        for result in results:
            fname.write(result)






if __name__ == '__main__':
    print(verilog2vhdl("DFFSR Q_int1_reg ( .D(serial_in), .CLK(clk), .R(1), .S(n5), .Q(Q_int1) )"))
    print(verilog2vhdl("  OAI22X1     U11  (.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25))"))
    print(verilog2vhdl("BAD(.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25))"))
    #print(verilog2vhdl("DFFSR Q_int1_reg ( .D(serial_in), .CLK(clk), .R(1), .S(n5), .Q(Q_int1) )"))
    #print(verilog2vhdl("DFFSR Q_int1_reg ( .D(serial_in), .CLK(clk), .R(1), .S(n5), .Q(Q_int1) )"))