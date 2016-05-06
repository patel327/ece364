#! /usr/local/bin/env python3.4

import sys
import os
import re

"""
def getRejectedUsers():
    with open("SiteRegistration.txt", "r") as fname:
        lines = fname.readlines()
        for line in lines:
            if re.search(r"(?P<whole>(?P<name>[a-zA-Z]+)([, ]+)(?P<name1>[a-zA-Z]+))([, ;]+)", line):
                m = re.search(r"(?P<whole>(?P<name>[a-zA-Z]+)([, ]+)(?P<name1>[a-zA-Z]+))([, ;]+)", line)
                print(m.group("whole"))
                #print(m.group("name1"))


def getUsersWithEmails():
    with open("SiteRegistration.txt", "r") as fname:
        dict = {}
        lines = fname.readlines()
        for line in lines:
            if re.search(r"@", line):
                m = re.search(r"(?P<whole>(?P<name>[a-zA-Z]+)([, ]+)(?P<name1>[a-zA-Z]+))([, ;]+)(?P<email>[a-z@_.0-9]+)([, ;]*)", line)
                print(m.group("email"))
                print(m.group("name"))
                print(m.group(("name1")))
                print(m.group("whole"))
                if re.search(r",", m.group("whole")):
                    dict[m.group("name1") + " " + m.group("name")] = m.group("email")
                else:
                    dict[m.group("name") + " " + m.group("name1")] = m.group("email")
        return dict

def getUsersWithPhones():
    with open("SiteRegistration.txt", "r") as fname:
        dict = {}
        lines = fname.readlines()
        for line in lines:
            if re.search("(?P<whole>(?P<name>[a-zA-Z]+)([, ]+)(?P<name1>[a-zA-Z]+))([, ;]+)(?P<email>[a-z@_.0-9]+)?([, ;]+)(?P<phone>[0-9() -]+)([, ;]+)", line):
                m = re.search("(?P<whole>(?P<name>[a-zA-Z]+)([, ]+)(?P<name1>[a-zA-Z]+))([, ;]+)(?P<email>[a-z@_.0-9]+)?([, ;]+)(?P<phone>[0-9() -]+)([, ;]+)", line)
                #if len(m.group("phone")) == 0:
                #phonee = "(" + (m.group("email"))[0:3] + ")" + " " + (m.group("email"))[3:6]+ "-" + (m.group("email"))[6:10]
                #print(phonee)
                print(m.group("name"))
                print(len(m.group("email")))
                if not re.search(r"[@]+", m.group("email")) and len(m.group("email")) != 0:
                    phone = "(" + (m.group("email"))[0:3] + ")" + " " + (m.group("email"))[3:6]+ "-" + (m.group("email"))[6:10]
                if re.search("[()]", m.group("phone")):
                    phone = m.group("phone")
                elif re.search("[-]", m.group("phone")):
                    phone = "(" + (m.group("phone"))[0:3] + ")" + " " + (m.group("phone"))[4:7]+ "-" + (m.group("phone"))[8:12]
                elif re.search(r"[@]+", m.group("email")):
                    phone = "(" + (m.group("phone"))[0:3] + ")" + " " + (m.group("phone"))[3:6]+ "-" + (m.group("phone"))[6:10]
                if len(m.group("phone")) > 3:
                    if re.search(r",", m.group("whole")):
                        dict[m.group("name1") + " " + m.group("name")] = phone
                    else:
                        dict[m.group("name") + " " + m.group("name1")] = phone
        return dict

"""

def getRejectedUsers():
    rlist = []
    with open("SiteRegistration.txt", "r") as fname:
        lines = fname.readlines()
        for line in lines:
            names =  re.search(r"(?P<whole>(?P<name1>[A-Z][a-z]+).?.?(?P<name2>[A-Z][a-z]+))[; ,]+(?P<email>[a-z0-9_.]+@purdue.com)?[; ,]+(?P<phone>\(?(?P<firstp>\d\d\d)[)-]? ?(?P<secondp>\d\d\d)-?(?P<thirdp>\d\d\d\d))?[; ,]*(?P<state>[A-Z][a-z]+ ?[A-Z]?[a-z]*)?", line)

            if names.group("email") is None and names.group("phone") is None and names.group("state") is None:
                if re.search(r",", names.group("whole")):
                    rlist.append(names.group("name2") + " " + names.group("name1"))
                else:
                    rlist.append(names.group("name1") + " " + names.group("name2"))
    rlist.sort()
    return rlist

def getUsersWithEmails():
    dict = {}
    with open("SiteRegistration.txt", "r") as fname:
        lines = fname.readlines()
        for line in lines:
            names =  re.search(r"(?P<whole>(?P<name1>[A-Z][a-z]+).?.?(?P<name2>[A-Z][a-z]+))[; ,]+(?P<email>[a-z0-9_.]+@purdue.com)?[; ,]+(?P<phone>\(?(?P<firstp>\d\d\d)[)-]? ?(?P<secondp>\d\d\d)-?(?P<thirdp>\d\d\d\d))?[; ,]*(?P<state>[A-Z][a-z]+ ?[A-Z]?[a-z]*)?", line)
            if not names.group("email") is None:
                if re.search(r",", names.group("whole")):
                    dict[names.group("name2") + " " + names.group("name1")] = names.group("email")
                else:
                    dict[names.group("name1") + " " + names.group("name2")] = names.group("email")
    return dict

def getUsersWithStates():
    dict = {}
    with open("SiteRegistration.txt", "r") as fname:
        lines = fname.readlines()
        for line in lines:
            names =  re.search(r"(?P<whole>(?P<name1>[A-Z][a-z]+).?.?(?P<name2>[A-Z][a-z]+))[; ,]+(?P<email>[a-z0-9_.]+@purdue.com)?[; ,]+(?P<phone>\(?(?P<firstp>\d\d\d)[)-]? ?(?P<secondp>\d\d\d)-?(?P<thirdp>\d\d\d\d))?[; ,]*(?P<state>[A-Z][a-z]+ ?[A-Z]?[a-z]*)?", line)
            if not names.group("state") is None:
                if re.search(r",", names.group("whole")):
                    dict[names.group("name2") + " " + names.group("name1")] = names.group("state")
                else:
                    dict[names.group("name1") + " " + names.group("name2")] = names.group("state")
    return dict

def getUsersWithPhones():
    dict = {}
    with open("SiteRegistration.txt", "r") as fname:
        lines = fname.readlines()
        for line in lines:
            names =  re.search(r"(?P<whole>(?P<name1>[A-Z][a-z]+).?.?(?P<name2>[A-Z][a-z]+))[; ,]+(?P<email>[a-z0-9_.]+@purdue.com)?[; ,]+(?P<phone>\(?(?P<firstp>\d\d\d)[)-]? ?(?P<secondp>\d\d\d)-?(?P<thirdp>\d\d\d\d))?[; ,]*(?P<state>[A-Z][a-z]+ ?[A-Z]?[a-z]*)?", line)
            if not names.group("phone") is None:
                if re.search(r",", names.group("whole")):
                    dict[names.group("name2") + " " + names.group("name1")] = "(" + names.group("firstp") + ")" + " " + names.group("secondp") + "-" + names.group("thirdp")
                else:
                    dict[names.group("name1") + " " + names.group("name2")] = "(" + names.group("firstp") + ")" + " " + names.group("secondp") + "-" + names.group("thirdp")
    return dict

def getUsersWithoutEmails():
    rlist = []
    with open("SiteRegistration.txt", "r") as fname:
        lines = fname.readlines()
        for line in lines:
            names =  re.search(r"(?P<whole>(?P<name1>[A-Z][a-z]+).?.?(?P<name2>[A-Z][a-z]+))[; ,]+(?P<email>[a-z0-9_.]+@purdue.com)?[; ,]+(?P<phone>\(?(?P<firstp>\d\d\d)[)-]? ?(?P<secondp>\d\d\d)-?(?P<thirdp>\d\d\d\d))?[; ,]*(?P<state>[A-Z][a-z]+ ?[A-Z]?[a-z]*)?", line)
            if names.group("email") is None and (not names.group("state") is None or not names.group("phone") is None):
                if re.search(r",", names.group("whole")):
                    rlist.append(names.group("name2") + " " + names.group("name1"))
                else:
                    rlist.append(names.group("name1") + " " + names.group("name2"))
    rlist.sort()
    return rlist

def getUsersWithoutPhones():
    rlist = []
    with open("SiteRegistration.txt", "r") as fname:
        lines = fname.readlines()
        for line in lines:
            names =  re.search(r"(?P<whole>(?P<name1>[A-Z][a-z]+).?.?(?P<name2>[A-Z][a-z]+))[; ,]+(?P<email>[a-z0-9_.]+@purdue.com)?[; ,]+(?P<phone>\(?(?P<firstp>\d\d\d)[)-]? ?(?P<secondp>\d\d\d)-?(?P<thirdp>\d\d\d\d))?[; ,]*(?P<state>[A-Z][a-z]+ ?[A-Z]?[a-z]*)?", line)
            if names.group("phone") is None and (not names.group("state") is None or not names.group("email") is None):
                if re.search(r",", names.group("whole")):
                    rlist.append(names.group("name2") + " " + names.group("name1"))
                else:
                    rlist.append(names.group("name1") + " " + names.group("name2"))
    rlist.sort()
    return rlist

def getUsersWithoutStates():
    rlist = []
    with open("SiteRegistration.txt", "r") as fname:
        lines = fname.readlines()
        for line in lines:
            names =  re.search(r"(?P<whole>(?P<name1>[A-Z][a-z]+).?.?(?P<name2>[A-Z][a-z]+))[; ,]+(?P<email>[a-z0-9_.]+@purdue.com)?[; ,]+(?P<phone>\(?(?P<firstp>\d\d\d)[)-]? ?(?P<secondp>\d\d\d)-?(?P<thirdp>\d\d\d\d))?[; ,]*(?P<state>[A-Z][a-z]+ ?[A-Z]?[a-z]*)?", line)
            if names.group("state") is None and (not names.group("phone") is None or not names.group("email") is None):
                if re.search(r",", names.group("whole")):
                    rlist.append(names.group("name2") + " " + names.group("name1"))
                else:
                    rlist.append(names.group("name1") + " " + names.group("name2"))
    rlist.sort()
    return rlist

def getUsersWithCompleteInfo():
    dict = {}
    with open("SiteRegistration.txt", "r") as fname:
        lines = fname.readlines()
        for line in lines:
            names =  re.search(r"(?P<whole>(?P<name1>[A-Z][a-z]+).?.?(?P<name2>[A-Z][a-z]+))[; ,]+(?P<email>[a-z0-9_.]+@purdue.com)?[; ,]+(?P<phone>\(?(?P<firstp>\d\d\d)[)-]? ?(?P<secondp>\d\d\d)-?(?P<thirdp>\d\d\d\d))?[; ,]*(?P<state>[A-Z][a-z]+ ?[A-Z]?[a-z]*)?", line)
            if not names.group("email") is None and not names.group("phone") is None and not names.group("state") is None:
                if re.search(r",", names.group("whole")):
                    dict[names.group("name2") + " " + names.group("name1")] = (names.group("email") ,"(" + names.group("firstp") + ")" + " " + names.group("secondp") + "-" + names.group("thirdp"), names.group("state"))
                else:
                    dict[names.group("name1") + " " + names.group("name2")] = (names.group("email") ,"(" + names.group("firstp") + ")" + " " + names.group("secondp") + "-" + names.group("thirdp"), names.group("state"))
    return dict

if __name__ == '__main__':
    getRejectedUsers()
    print(sys.version)
    #getUsersWithPhones()