#! /usr/local/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2016-02-03 11:42:05 -0500 (Wed, 03 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Lab03/simpleTasks.py $
#$Revision: 87631 $

import sys
import os
import math

def getPairwiseDifference(vec):
    if type(vec) is not list: #if type(vec) == "list":
        return None
    if len(vec) == 0:
        return None
    j = 0
    newL = [1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9]
    #print(type(newL))
    while j < (len(vec) - 1):
        #print(type(vec[j]))
        newL[j] = int(vec[j+1]) - int(vec[j])
        j+=1
    return newL[:(len(vec) - 1)]

def flatten(l):
    if type(l) is not list:
        return None
    for j in l:
        if type(j) is not list:
            return None
    newL = []
    for g in l:
        newL += g
    return newL

def partition(l, n):
    if type(l) is not list:
        return None
    if len(l) == 0:
        return None
    newLL = [[],[],[],[],[],[],[],[]]
    j = 0
    while len(l) > n:
        newLL[j] += l[:n]
        j+=1
        del l[:n]
    newLL[j] = l[:]
    return newLL[:j+1]

def rectifySignal(v):
    if type(v) is not list:
        return None
    if len(v) == 0:
        return None
    for j in v:
        if j < 0:
            e = v.index(j)
            v[e] = 0
    return v

def floatRange(a, b, s):
    if a >= b:
        return None
    newL = [a]
    j = a
    while j < b:
        j += s
        j = round(j, 1)
        newL.append(j)
    return newL

def getLongestWord(s):
    if type(s) is not str:
        return None
    l = s.split()
    if len(l) < 2:
        return None
    greatest = 0
    for j in l:
        if len(j) > greatest:
            longest = j
            greatest = len(j)
    return longest

def decodeNumbers(numList):
    if type(numList) is not list:
        return None
    for j in numList:
        if type(j) is not int:
            return None
    word = ""
    for j in numList:
        print(chr(j))
        word = word + str(chr(j))
    return word

def getCreditCard(s):
    if len(s) < 1:
        return None
    newL = []
    s = s.split()
    for j in s:
        for c in j:
            if(ord(c) >= 48 and ord(c) <= 57):
                print(ord(c))
                newL.append(int(c))
    return newL




if __name__ == "__main__":
    #g = getPairwiseDifference([16, 10, 27, 4, 7, 3, 24, 13, 27, 21])
    #print(g)
    #decodeNumbers([69, 67, 69, 51, 54, 52, 32, 115, 104, 111, 117, 108, 100, 32, 98, 101, 32, 109, 111, 114, 101, 32, 116, 104, 97, 110, 32, 49, 32, 67, 114, 101, 100, 105, 116, 32, 72, 111, 117, 114, 33])
    getCreditCard("abbb1 234")
    pass