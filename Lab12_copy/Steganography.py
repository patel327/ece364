#! /usr/bin/env python3.4
#
#$Author: ee364e07 $
#$Date: 2016-04-11 16:57:02 -0400 (Mon, 11 Apr 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364e07/Lab11/Steganography.py $
#$Revision: 90437 $

import sys
import re
import numpy as np
import base64
import zlib
from scipy.misc import *



def test():
    print(sys.version)

class Payload:

    def __init__(self, img=None, compressionLevel=-1, xml=None):

        if compressionLevel > 9  or compressionLevel < -1:
            raise ValueError("Bad Compression")
        try:
            if img.any():
                if type(img).__module__ != np.__name__:
                    raise TypeError("Image is not ndarray")
                self.img = img
                self.xml = Payload.generateXML(self,compressionLevel)
            elif xml:
                if type(xml) != str:
                    raise TypeError("Xml is not string")
                self.xml = xml
                self.img = Payload.generateIMG(self, self.xml)
            else:
                raise ValueError("Both image and xml not provided")
        except:
            if img:
                if type(img).__module__ != np.__name__:
                    raise TypeError("Image is not ndarray")
                self.img = img
                self.xml = Payload.generateXML(self,compressionLevel)
            elif xml:
                if type(xml) != str:
                    raise TypeError("Xml is not string")
                self.xml = xml
                self.img = Payload.generateIMG(self, self.xml)
            else:
                raise ValueError("Both image and xml not provided")

    def generateIMG(self, xmlstr):
        listofstr = xmlstr.split("\n")
        content = listofstr[2].strip()
        q = re.search(r'[^"]+\"([^"]+)\"[^"]+\"([^"]+)\"[^"]+\"([^"]+)\"',listofstr[1])
        ptype = q.group(1)
        size = q.group(2)
        comp = q.group(3)
        decd = base64.b64decode(content)
        if comp == "True":
            decomp = zlib.decompress(decd)
        else:
            decomp = decd
        sizes = size.split(",")
        imagel =None
        if ptype == "Gray":
            imagel = np.array(list(decomp))
            imagel = np.resize(imagel, (int(sizes[0]), int(sizes[1])))

        if ptype == "Color":
            imagel = np.array(list(decomp))
            offse = len(imagel)/3
            totalc = []
            for x in range(int(offse)):
                totalc.append(imagel[x])
                totalc.append(imagel[x+offse])
                totalc.append(imagel[x+offse*2])

            imagel = np.resize(np.array(totalc), (int(sizes[0]), int(sizes[1]), 3))
        return imagel

    def generateXML(self, compressionLevel):
        xmlstr = '<?xml version="1.0" encoding="UTF-8"?>\n' + '<payload type="'
        if self.img.ndim ==2:
            xmlstr += 'Gray'
        elif self.img.ndim == 3:
            xmlstr += 'Color'
        else:
            print("why here/generateXML")

        xmlstr += '" size="'
        if self.img.ndim ==2:
            xmlstr += str(self.img.shape)[1:-1].replace(" ", "")
        else:
            xmlstr += str(self.img.shape)[1:-4].replace(" ", "")
        xmlstr += '" compressed="'
        if compressionLevel == -1:
            xmlstr += 'False">\n'
        elif compressionLevel >-1 and compressionLevel < 10:
            xmlstr += 'True">\n'
        else:
            print("nonono/generateXML")
        content = None
        if self.img.ndim ==2:
            content = self.img.reshape(1, -1)
            if compressionLevel == -1:
                stringer = content
            else:
                stringer = zlib.compress(content, compressionLevel)
            b64s = base64.b64encode(stringer)
            xmlstr += str(b64s.decode("utf-8")) + "\n"
            xmlstr += '</payload>'

        else:
            red = []
            green = []
            blue = []
            for row in range(self.img.shape[0]):
                for col in range(self.img.shape[1]):
                    red.append(self.img[row][col][0])
                    green.append(self.img[row][col][1])
                    blue.append(self.img[row][col][2])
            full = red + green + blue
            fullnd = np.array(full)
            if compressionLevel == -1:
                stringer = fullnd
            else:
                stringer = zlib.compress(fullnd, compressionLevel)
            b64s = base64.b64encode(stringer)
            xmlstr += str(b64s.decode("utf-8")) + "\n"
            xmlstr += '</payload>'
        return xmlstr

    def getSize(self):
        listofstr = self.xml.split("\n")
        q = re.search(r'[^"]+\"([^"]+)\"[^"]+\"([^"]+)\"[^"]+\"([^"]+)\"',listofstr[1])
        sizes = q.group(2).split(",")
        return int(sizes[0]) * int(sizes[1])



class Carrier:

    def __init__(self, img):
        self.img = img
        if type(img) != np.ndarray:
            raise TypeError("Carrier: img is not NDarray")

    def payloadExists(self):
        pay = np.bitwise_and(self.img, 1)
        if pay.ndim ==2:
            newpay = np.reshape(pay, (-1, 1))
            pack = np.packbits(newpay)
            xml = ''.join(chr(i) for i in pack)
            realxml = xml.split(">")
            realxml = '>'.join(str(i) for i in realxml[:3]) + '>'
            if realxml.split("\n")[0] == '<?xml version="1.0" encoding="UTF-8"?>':
                return True
            return False
            #return Payload(xml=realxml)
        else:
            red = []
            green = []
            blue = []
            for row in range(pay.shape[0]):
                for col in range(pay.shape[1]):
                    red.append(pay[row][col][0])
                    green.append(pay[row][col][1])
                    blue.append(pay[row][col][2])
            full = red + green + blue
            fullnd = np.array(full)
            newpay = np.reshape(fullnd, (-1, 1))
            pack = np.packbits(newpay)
            xml = ''.join(chr(i) for i in pack)
            realxml = xml.split(">")
            realxml = '>'.join(str(i) for i in realxml[:3]) + '>'
            if realxml.split("\n")[0] == '<?xml version="1.0" encoding="UTF-8"?>':
                return True
            return False

    def clean(self):
        return np.bitwise_and(self.img, 254)


    def embedPayload(self, payload, override=False):
        if type(payload) != Payload:
            raise TypeError ("payload given is not an instance of Payload")
        if self.img.ndim ==2:
            if self.img.shape[0] * self.img.shape[1] < len(payload.xml) * 8:
                raise ValueError("payload is too big")
        else:
            if self.img.shape[0] * self.img.shape[1] * self.img.shape[2] < len(payload.xml) * 8:
                raise ValueError("payload is too big")
        if self.payloadExists() and override == False:
            raise Exception("payload exists, override is false")
        xmlstr = payload.xml
        xmlasc = [ord(c) for c in xmlstr]
        xmlbit = [bin(c)[2:].zfill(8) for c in xmlasc]
        if self.img.ndim == 2:
            newimg = np.reshape(self.img.copy(), (-1, 1))
            for x in range(0,len(xmlbit)):
                if int(xmlbit[x][0]) == 1:
                    newimg[8*x][0] = (newimg[8*x][0] | 1)
                else:
                    newimg[8*x][0] = (newimg[8*x][0] & 254)

                if int(xmlbit[x][1]) == 1:
                    newimg[8*x +1][0] = (newimg[8*x +1][0] | 1)
                else:
                    newimg[8*x +1][0] = (newimg[8*x +1][0] & 254)

                if int(xmlbit[x][2]) == 1:
                    newimg[8*x +2][0] = (newimg[8*x +2][0] | 1)
                else:
                    newimg[8*x +2][0] = (newimg[8*x +2][0] & 254)

                if int(xmlbit[x][3]) == 1:
                    newimg[8*x +3][0] = (newimg[8*x +3][0] | 1)
                else:
                    newimg[8*x +3][0] = (newimg[8*x +3][0] & 254)

                if int(xmlbit[x][4]) == 1:
                    newimg[8*x +4][0] = (newimg[8*x +4][0] | 1)
                else:
                    newimg[8*x +4][0] = (newimg[8*x +4][0] & 254)

                if int(xmlbit[x][5]) == 1:
                    newimg[8*x +5][0] = (newimg[8*x +5][0] | 1)
                else:
                    newimg[8*x +5][0] = (newimg[8*x +5][0] & 254)

                if int(xmlbit[x][6]) == 1:
                    newimg[8*x +6][0] = (newimg[8*x +6][0] | 1)
                else:
                    newimg[8*x +6][0] = (newimg[8*x +6][0] & 254)

                if int(xmlbit[x][7]) == 1:
                    newimg[8*x +7][0] = (newimg[8*x +7][0] | 1)
                else:
                    newimg[8*x +7][0] = (newimg[8*x +7][0] & 254)
            finalimg = np.reshape(newimg, self.img.shape)
            return finalimg
        else:
            red = []
            green = []
            blue = []
            for row in range(self.img.shape[0]):
                for col in range(self.img.shape[1]):
                    red.append(self.img[row][col][0])
                    green.append(self.img[row][col][1])
                    blue.append(self.img[row][col][2])
            full = red + green + blue
            fullnd = np.array(full)
            newimg = np.reshape(fullnd.copy(), (-1, 1))
            for x in range(0,len(xmlbit)):
                if int(xmlbit[x][0]) == 1:
                    newimg[8*x][0] = (newimg[8*x][0] | 1)
                else:
                    newimg[8*x][0] = (newimg[8*x][0] & 254)

                if int(xmlbit[x][1]) == 1:
                    newimg[8*x +1][0] = (newimg[8*x +1][0] | 1)
                else:
                    newimg[8*x +1][0] = (newimg[8*x +1][0] & 254)

                if int(xmlbit[x][2]) == 1:
                    newimg[8*x +2][0] = (newimg[8*x +2][0] | 1)
                else:
                    newimg[8*x +2][0] = (newimg[8*x +2][0] & 254)

                if int(xmlbit[x][3]) == 1:
                    newimg[8*x +3][0] = (newimg[8*x +3][0] | 1)
                else:
                    newimg[8*x +3][0] = (newimg[8*x +3][0] & 254)

                if int(xmlbit[x][4]) == 1:
                    newimg[8*x +4][0] = (newimg[8*x +4][0] | 1)
                else:
                    newimg[8*x +4][0] = (newimg[8*x +4][0] & 254)

                if int(xmlbit[x][5]) == 1:
                    newimg[8*x +5][0] = (newimg[8*x +5][0] | 1)
                else:
                    newimg[8*x +5][0] = (newimg[8*x +5][0] & 254)

                if int(xmlbit[x][6]) == 1:
                    newimg[8*x +6][0] = (newimg[8*x +6][0] | 1)
                else:
                    newimg[8*x +6][0] = (newimg[8*x +6][0] & 254)

                if int(xmlbit[x][7]) == 1:
                    newimg[8*x +7][0] = (newimg[8*x +7][0] | 1)
                else:
                    newimg[8*x +7][0] = (newimg[8*x +7][0] & 254)
            offse = len(newimg)/3
            totalc = []
            for x in range(int(offse)):
                totalc.append(newimg[x])
                totalc.append(newimg[x+offse])
                totalc.append(newimg[x+offse*2])

            finalimg = np.resize(np.array(totalc), (self.img.shape[0], self.img.shape[1], 3))
            return finalimg

    def extractPayload(self):
        if  not self.payloadExists():
            raise Exception("no")
        pay = np.bitwise_and(self.img, 1)
        if pay.ndim ==2:
            newpay = np.reshape(pay, (-1, 1))
            pack = np.packbits(newpay)
            xml = ''.join(chr(i) for i in pack)
            realxml = xml.split(">")
            realxml = '>'.join(str(i) for i in realxml[:3]) + '>'
            return Payload(xml=realxml)
        else:
            red = []
            green = []
            blue = []
            for row in range(pay.shape[0]):
                for col in range(pay.shape[1]):
                    red.append(pay[row][col][0])
                    green.append(pay[row][col][1])
                    blue.append(pay[row][col][2])
            full = red + green + blue
            fullnd = np.array(full)
            newpay = np.reshape(fullnd, (-1, 1))
            pack = np.packbits(newpay)
            xml = ''.join(chr(i) for i in pack)
            realxml = xml.split(">")
            realxml = '>'.join(str(i) for i in realxml[:3]) + '>'
            return Payload(xml=realxml)

if __name__ == "__main__":
    #print(sys.version)
    imgr = imread("test_images/result1.png")
    print(imgr)#[888][2550:2560])
    imgtest = imread("test_images/payload1.png")
    #print(imgtest)
    #print(imgtest.shape)
    #with open("test_images/payload2_-1.xml", "r") as f:
    #    xmls = f.read()
        #print(type(xmls))
        #print(xmls)
    #p = Payload(img = imgtest, compressionLevel= 9)
    #print(len(p.xml))
    #xml = getXML(join(self.folder, "payload1_-1.xml"))
    #with open(path, "r") as xFile:
    #    content = xFile.read()
    #p = Payload(xml = xmls)
    #print(p.img)
    #for row in p.img:
    #    print(row)

    #print(p.xml)
    #img = imread("test_images/result2.png")
    #c = Carrier(img)
    #c.extractPayload()
    p = Payload(imgtest, 9)
    c = Carrier(imread("test_images/carrier1.png"))
    c.embedPayload(p)
    #print(c.img.shape)
