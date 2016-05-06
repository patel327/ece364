#! /usr/local/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2016-02-17 11:19:59 -0500 (Wed, 17 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Lab05/practical1.py $
#$Revision: 88353 $

import sys
import os
import math
import glob
import string
import filecmp

def rowSumIsValid(mat):
    sumlist = []
    sumr = [sum(x) for x in mat]
    ver = sumr[0]
    for item in sumr:
        if item != ver:
            return False
    #print(sumr)
    return True

def columnSumIsValid(mat):
    sumc = [sum(x) for x in zip(*mat)]
    ver = sumc[0]
    for item in sumc:
        if item != ver:
            return False
    return True

def magicSquareIsValid(filePath):
    msq = []
    temp = []
    with open(filePath, "r") as fname:
        lines = fname.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                temp.append(int(word))
            msq.append(temp)
            temp = []
    print(msq)
    bool1 = rowSumIsValid(msq)
    bool2 = columnSumIsValid(msq)
    if bool1 == False or bool2 == False:
        return False
    return True



def getcostdic(path):
    dict = {}
    with open(path, "r") as fname:
        lines = fname.readlines()
        for line in lines[3:]:
            words = line.split(",")
            #print(words)
            name = words[0].strip()
            #print(name)
            price = (words[1]).split("$")
            price = price[1].strip()
            #print(price)
            dict[name] = float(price)
    return dict


def getTotalCost(itemSet):
    amazond = getcostdic("Stores/Amazon.txt")
    jetd = getcostdic("Stores/Jet.txt")
    neweggd = getcostdic("Stores/NewEgg.txt")
    tigerdirectd = getcostdic("Stores/TigerDirect.txt")
    walmartd = getcostdic("Stores/WalMart.txt")
    total = 0.0
    cost = 0.0
    totcost = {}

    for item in itemSet:
        cost = float(amazond[item[0]] * item[1])
        cost = round(cost, 2)
        total += cost
        total = round(total, 2)
    totcost["Amazon"] = total

    total = 0.0
    for item in itemSet:
        cost = float(jetd[item[0]] * item[1])
        cost = round(cost, 2)
        total += cost
        total = round(total, 2)
    totcost["Jet"] = total

    total = 0.0
    for item in itemSet:
        cost = float(neweggd[item[0]] * item[1])
        cost = round(cost, 2)
        total += cost
        total = round(total, 2)
    totcost["NewEgg"] = total

    total = 0.0
    for item in itemSet:
        cost = float(tigerdirectd[item[0]] * item[1])
        cost = round(cost, 2)
        total += cost
        total = round(total, 2)
    totcost["TigerDirect"] = total

    total = 0.0
    for item in itemSet:
        cost = float(walmartd[item[0]] * item[1])
        cost = round(cost, 2)
        total += cost
        total = round(total, 2)
    totcost["WalMart"] = total

    return totcost

def getBestPrices(cpuSet):
    amazond = getcostdic("Stores/Amazon.txt")
    jetd = getcostdic("Stores/Jet.txt")
    neweggd = getcostdic("Stores/NewEgg.txt")
    tigerdirectd = getcostdic("Stores/TigerDirect.txt")
    walmartd = getcostdic("Stores/WalMart.txt")

    bestdict = {}

    for item in cpuSet:
        if item in amazond:
            aprice = amazond[item]
        else:
            aprice = 10000

        if item in jetd:
            jprice = jetd[item]
        else:
            jprice = 10000

        if item in neweggd:
            nprice = neweggd[item]
        else:
            nprice = 10000

        if item in tigerdirectd:
            tprice = tigerdirectd[item]
        else:
            tprice = 10000

        if item in walmartd:
            wprice = walmartd[item]
        else:
            wprice = 10000

        if aprice < jprice and aprice < nprice and aprice < tprice and aprice < wprice:
            bestdict[item] = (aprice, "Amazon")
        elif jprice < nprice and jprice < tprice and jprice < wprice:
            bestdict[item] = (jprice, "Jet")
        elif nprice < tprice and nprice < wprice:
            bestdict[item] = (nprice, "NewEgg")
        elif tprice < wprice:
            bestdict[item] = (tprice, "TigerDirect")
        else:
            bestdict[item] = (wprice, "WalMart")
    return bestdict

def getMissingItems():
    amazond = getcostdic("Stores/Amazon.txt")
    jetd = getcostdic("Stores/Jet.txt")
    neweggd = getcostdic("Stores/NewEgg.txt")
    tigerdirectd = getcostdic("Stores/TigerDirect.txt")
    walmartd = getcostdic("Stores/WalMart.txt")

    listofall = []
    listofall.extend(amazond.keys())
    listofall.extend(jetd.keys())
    listofall.extend(neweggd.keys())
    listofall.extend(tigerdirectd.keys())
    listofall.extend(walmartd.keys())
    alist = set()
    jlist = set()
    nlist = set()
    tlist = set()
    wlist = set()
    print(listofall)

    setofall = set(listofall)
    dict = {}

    for item in setofall:
        if not item in amazond:
            alist.add(item)
        if not item in jetd:
            jlist.add(item)
        if not item in neweggd:
            nlist.add(item)
        if not item in tigerdirectd:
            tlist.add(item)
        if not item in walmartd:
            wlist.add(item)
    dict["Amazon"] = alist
    dict["Jet"] = jlist
    dict["NewEgg"] = nlist
    dict["TigerDirect"] = tlist
    dict["WalMart"] = wlist

    return dict

if __name__ == '__main__':
    square4 = [[16, 2, 3, 13],
           [5, 11, 10, 1],
           [9, 7, 6, 12],
           [4, 14, 15, 8]]
    square6 = [[35, 1, 6, 26, 19, 24],
           [3, 25, 7, 21, 23, 32],
           [31, 9, 2, 22, 27, 20],
           [8, 28, 33, 17, 10, 15],
           [30, 5, 34, 12, 14, 16],
           [4, 36, 29, 13, 18, 11]]
    #print(columnSumIsValid(square4))
    #magicSquareIsValid("Squares/magic4.txt")
    #getcostdic("Stores/Amazon.txt")
    #itemSet = {('Intel i7-4702HQ', 8), ('Intel i7-4710MQ', 9), ('Intel i7-4700EC', 9), ('Intel i7-6600U', 7)}
    #actualValue = getTotalCost(itemSet)
    getMissingItems()