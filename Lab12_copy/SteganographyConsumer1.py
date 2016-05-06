#! /usr/bin/env python3.4
#
#$Author$
#$Date$
#$HeadURL$
#$Revision$


import sys

from PySide.QtGui import *
from SteganographyGUI import *
from Steganography import *
import re
import os

class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.setAcceptDrops(True)
        self.viewPayload1.installEventFilter(self)
        self.viewCarrier1.installEventFilter(self)
        self.viewCarrier2.installEventFilter(self)
        self.viewPayload2.installEventFilter(self)



    def eventFilter(self, obj, event):
        if obj == self.viewPayload1:
            if event.type() == QtCore.QEvent.DragEnter:
                event.accept()
                return True
            elif event.type() == QtCore.QEvent.DragMove:
                event.accept()
                return True
            elif event.type() == QtCore.QEvent.Drop:
                event.accept()

                fpath = str(event.mimeData().urls()[0]).split("'")[1].split(":")[1][2:]
                if 'png' in fpath.split('.')[1]:
                    img = QImage(fpath)
                    pixmap = QtGui.QPixmap(fpath)
                    pixmap = pixmap.scaled(358, 278, QtCore.Qt.KeepAspectRatio)
                    pixItem = QtGui.QGraphicsPixmapItem(pixmap)
                    scn = QtGui.QGraphicsScene()
                    scn.addItem(pixItem)
                    self.viewPayload1.setScene(scn)
                return True
            else:
                event.ignore()
                return False
        elif obj == self.viewCarrier1:
            if event.type() == QtCore.QEvent.DragEnter:
                event.accept()
                return True
            elif event.type() == QtCore.QEvent.DragMove:
                event.accept()
                return True
            elif event.type() == QtCore.QEvent.Drop:
                event.accept()

                fpath = str(event.mimeData().urls()[0]).split("'")[1].split(":")[1][2:]
                if 'png' in fpath.split('.')[1]:
                    pixmap = QtGui.QPixmap(fpath)
                    pixmap = pixmap.scaled(358, 278, QtCore.Qt.KeepAspectRatio)
                    pixItem = QtGui.QGraphicsPixmapItem(pixmap)
                    scn = QtGui.QGraphicsScene()
                    scn.addItem(pixItem)
                    self.viewCarrier1.setScene(scn)
                return True
            else:
                event.ignore()
                return False

        elif obj == self.viewCarrier2:
            if event.type() == QtCore.QEvent.DragEnter:
                event.accept()
                return True
            elif event.type() == QtCore.QEvent.DragMove:
                event.accept()
                return True
            elif event.type() == QtCore.QEvent.Drop:
                event.accept()

                fpath = str(event.mimeData().urls()[0]).split("'")[1].split(":")[1][2:]
                if 'png' in fpath.split('.')[1]:
                    img = QImage(fpath)
                    pixmap = QtGui.QPixmap(fpath)
                    pixmap = pixmap.scaled(358, 278, QtCore.Qt.KeepAspectRatio)
                    pixItem = QtGui.QGraphicsPixmapItem(pixmap)
                    scn = QtGui.QGraphicsScene()
                    scn.addItem(pixItem)
                    self.viewCarrier2.setScene(scn)
                return True
            else:
                event.ignore()
                return False

        elif obj == self.viewPayload2:
            if event.type() == QtCore.QEvent.DragEnter:
                keyEvent = event
                event.accept()
                return True
            elif event.type() == QtCore.QEvent.DragMove:
                event.accept()
                return True
            elif event.type() == QtCore.QEvent.Drop:
                event.accept()

                fpath = str(event.mimeData().urls()[0]).split("'")[1].split(":")[1][2:]
                if 'png' in fpath.split('.')[1]:
                    img = QImage(fpath)
                    pixmap = QtGui.QPixmap(fpath)
                    pixmap = pixmap.scaled(358, 278, QtCore.Qt.KeepAspectRatio)
                    pixItem = QtGui.QGraphicsPixmapItem(pixmap)
                    scn = QtGui.QGraphicsScene()
                    scn.addItem(pixItem)
                    self.viewPayload2.setScene(scn)
                return True
            else:
                event.ignore()
                return False
        else:
            # pass the event on to the parent class
            return QMainWindow.eventFilter(self, obj, event)




if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()