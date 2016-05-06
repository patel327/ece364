#! /usr/local/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2016-02-10 12:04:11 -0500 (Wed, 10 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Lab04/registrar.py $
#$Revision: 88063 $

import sys
import os
import math
import glob
import string
import filecmp

def getDetails():
    sdict = studentDict()
    files = glob.glob("files/EE*.txt")
    key = {}
    for file in files:
        with open(file, "r") as fname:
            lines = fname.readlines()
            for line in lines[2:]:
                #print(line)
                words = line.split()
                tups = set()
                for keys, value in sdict.items():

                    if words[0] == value:
                        if keys not in key:
                            tuple = (file[10:13], int(words[1]))
                            #print(tuple)
                            tups.add(tuple)
                            key[keys] = set()
                            key[keys].add(tuple)
                        else:
                            tuple = (file[10:13], int(words[1]))
                            key[keys].add(tuple)
    return key



def getStudentList(classNumber):
    file = "files/EECS%s.txt" % classNumber
    if not os.path.exists(file):
        return[]
    sdict = studentDict()
    listofs = []
    with open(file, "r")as fname:
        lines = fname.readlines()
        for line in lines[2:]:
            words = line.split()
            for word in words[::2]:
                print(word)
                for keys, values in sdict.items():
                    if values == word:
                        listofs.append(keys)
                        print(listofs)
                        break
    print("here")
    print(listofs)
    print(sorted(listofs))
    return sorted(listofs)


def searchForName(studentName):
    sdict = studentDict()
    ndict = {}
    if not studentName in sdict.keys():
        return ndict
    files = glob.glob("files/EE*.txt")
    dict = getDetails()
    for tuples in dict[studentName]:
        classs, grade = tuples
        ndict[classs] = grade
    return ndict

def searchForID(studentID):
    sdict = studentDict()
    Idict = {}
    ID = IDDict()
    if not studentID in sdict.values():
        return Idict
    dict = getDetails()
    print(type(studentID))
    if studentID not in ID:
        return {}
    else:
        name = ID[studentID]

    print(name)
    for tuples in dict[name]:
        print(tuples)
        classs, grade = tuples
        Idict[classs] = grade
    return Idict

def findScore(studentName, classNumber):
    file = "files/EECS%s.txt" % classNumber
    if not os.path.exists(file):
        return None
    ID = IDDict()
    with open(file, "r") as fname:
        lines = fname.readlines()
        for line in lines[2:]:
            word = line.split()
            name = ID[word[0]]
            if name == studentName:
                return int(word[1])
    return None

def getHighest(classNumber):
    file = "files/EECS%s.txt" % classNumber
    if not os.path.exists(file):
        return ()
    ID = IDDict()
    max = 0
    with open(file, "r") as fname:
        lines = fname.readlines()
        for line in lines[2:]:
            words = line.split()
            if int(words[1]) > max:
                max = int(words[1])
                name = ID[words[0]]
    return(name, max)

def getLowest(classNumber):
    file = "files/EECS%s.txt" % classNumber
    if not os.path.exists(file):
        return ()
    ID = IDDict()
    min = 100000
    with open(file, "r") as fname:
        lines = fname.readlines()
        for line in lines[2:]:
            words = line.split()
            if int(words[1]) < min:
                min = int(words[1])
                name = ID[words[0]]
    return(name, min)

def getAverageScore(studentName):
    files = glob.glob("files/EE*.txt")
    sum = 0
    num = 0
    avg = 0.0
    ID = IDDict()
    sdict = studentDict()
    print("here")
    #print(sdict["goku"])
    for file in files:
        with open(file, "r") as fname:
            lines = fname.readlines()
            for line in lines[2:]:
                words = line.split()
                if studentName == ID[words[0]]:
                    sum += int(words[1])
                    num += 1
    if num == 0:
        return None
    avg = sum/num
    return avg


def studentDict():
    files = glob.glob("files/students.txt")
    dict = {}
    for file in files:
        with open(file, "r") as fname:
            lines = fname.readlines()
            for line in lines[2:]:
                #print(line)
                line = line.strip()
                words = line.split()
                dict[words[0] + " " + words [1] + " " + words [2]] = words[4]
    return dict
def IDDict():
    files = glob.glob("files/students.txt")
    dict = {}
    for file in files:
        with open(file, "r") as fname:
            lines = fname.readlines()
            for line in lines[2:]:
                #print(line)
                line = line.strip()
                words = line.split()
                dict[words[4]] = words[0] + " " + words [1] + " " + words [2]
    return dict

if __name__ == '__main__':
    print(sys.version)
    s = studentDict()
    print(s)
    #key = getDetails()
    #print(key)
    #A = getStudentList(370)
    #print("output")
    #print(A)
    getAverageScore("goku")
    print(searchForID("63581-09884"))
