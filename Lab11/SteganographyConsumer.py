import sys
from functools import partial
from os.path import splitext
from SteganographyGUI import *
from PySide.QtCore import *
from PySide.QtGui import *
from Steganography import *
import os


class SteganographyConsumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(SteganographyConsumer, self).__init__(parent)
        self.setupUi(self)

        self.pf = 0
        self.qf = 0

        self.slideCompression.valueChanged.connect(self.evalSlide)
        self.chkApplyCompression.stateChanged.connect(self.chek)
        self.chkOverride.stateChanged.connect(self.evalEmbed)
        self.btnSave.clicked.connect(self.saveImage)
        self.btnClean.clicked.connect(self.cleanImage)
        self.btnExtract.clicked.connect(self.extractImage)

        # Get the views that are required to have the drag-and-drop enabled.
        views = [self.viewPayload1, self.viewCarrier1, self.viewCarrier2]
        accept = lambda e: e.accept()

        for view in views:
            # We need to accept the drag event to be able to accept the drop.
            view.dragEnterEvent = accept
            view.dragMoveEvent = accept
            view.dragLeaveEvent = accept

            # Assign an event handler (a method,) to be invoked when a drop is performed.
            view.dropEvent = partial(self.processDrop, view)

        # NOTE: The line above links "all" views to the same function, and passes the view as a parameter in the
        # function. You could pass more than one widget to the function by adding more parameters to the signature,
        # in case you want to bind more than one widget together. you can even pass in another function, as a parameter,
        # which might significantly reduce the size of your code. Finally, if you prefer to have a separate function
        # for each view, where the view name is, say, "someView", you will need to:
        # 1- Create a function with a definition similar: funcName(self, e)
        # 2- Assign the function to be invoked as the event handler:
        #   self.someView.dropEvent = self.funcName

    def chek(self):
        if self.chkApplyCompression.isChecked():
            self.lblLevel.setEnabled(True)
            self.slideCompression.setEnabled(True)
            self.txtCompression.setEnabled(True)
            self.p = Payload(img=self.p.img, compressionLevel=self.slideCompression.value())
            lengt = len(self.p.xml)
            self.txtPayloadSize.setText(str(lengt))
            self.evalEmbed()
        else:
            self.lblLevel.setEnabled(False)
            self.slideCompression.setEnabled(False)
            self.txtCompression.setEnabled(False)
            self.p = Payload(img=self.p.img)
            lengt = len(self.p.xml)
            self.txtPayloadSize.setText(str(lengt))
            self.evalEmbed()



    def processDrop(self, view, e):
        """
        Process a drop event when it occurs on the views.
        """
        mime = e.mimeData()

        # Guard against types of drops that are not pertinent to this app.
        if not mime.hasUrls():
            return

        # Obtain the file path using the OS format.
        filePath = mime.urls()[0].toLocalFile()
        _, ext = splitext(filePath)

        if not ext == ".png":
            return

        # Now the file path is ready to be processed.
        #
        # TODO: Remove the print statement and continue the implementation using the filePath.
        #
        print(filePath)
        pixmap = QtGui.QPixmap(filePath)
        pixmap = pixmap.scaled(358, 278, QtCore.Qt.KeepAspectRatio)
        pixItem = QtGui.QGraphicsPixmapItem(pixmap)
        scn = QtGui.QGraphicsScene()
        scn.addItem(pixItem)
        view.setScene(scn)




        print(view)
        if view == self.viewPayload1:
            self.chkApplyCompression.setCheckState(QtCore.Qt.Unchecked)
            self.lblLevel.setEnabled(False)
            self.slideCompression.setEnabled(False)
            self.slideCompression.setValue(0)
            self.txtCompression.setEnabled(False)
            self.txtCompression.setText("0")
            img = imread(filePath)
            self.p = Payload(img=img)
            lengt = len(self.p.xml)
            #with open("t.txt", "wb")as f:
            #    f.write(bytes(self.p.xml, 'UTF-8'))
            self.txtPayloadSize.setText(str(lengt))
            self.pf = 1
            self.evalEmbed()

        if view == self.viewCarrier1:
            self.lblPayloadFound.setText("")
            self.chkOverride.setEnabled(False)
            self.chkOverride.setCheckState(QtCore.Qt.Unchecked)
            img = imread(filePath)
            self.q = Carrier(img=img)
            if self.q.img.ndim == 2:
                lengt = self.q.img.shape[0] * self.q.img.shape[1] / 8
            else:
                lengt = self.q.img.shape[0] * self.q.img.shape[1] * self.q.img.shape[2] / 8
            self.txtCarrierSize.setText(str(int(lengt)))
            if self.q.payloadExists():
                self.lblPayloadFound.setText(">>>>Payload Found<<<<")
                self.chkOverride.setEnabled(True)
                self.chkOverride.setCheckState(QtCore.Qt.Checked)
            self.qf = 1
            self.evalEmbed()

        if view == self.viewCarrier2:
            self.filePath = filePath
            self.lblCarrierEmpty.setText("")
            self.btnClean.setEnabled(False)
            self.btnExtract.setEnabled(False)
            #for i in range(50000):
            #    pass
            img = imread(filePath)
            self.q2 = Carrier(img=img)
            if self.q2.payloadExists():
                self.btnClean.setEnabled(True)
                self.btnExtract.setEnabled(True)
            else:
                self.lblCarrierEmpty.setText(">>>>Carrier Empty<<<<")
            self.viewPayload2.setScene(QtGui.QGraphicsScene())




    def evalEmbed(self):
        print("we eval")
        if self.qf and self.pf:
            if int(self.txtPayloadSize.text()) < int(self.txtCarrierSize.text()):
                if not self.chkOverride.isEnabled() or self.chkOverride.isChecked():
                    print("yes we can")
                    self.btnSave.setEnabled(True)
                else:
                    self.btnSave.setEnabled(False)
            else:
                self.btnSave.setEnabled(False)
        else:
            self.btnSave.setEnabled(False)



    def evalSlide(self):
        print(int(self.slideCompression.value()))
        self.txtCompression.setText(str(self.slideCompression.value()))
        self.p = Payload(img=self.p.img, compressionLevel=self.slideCompression.value())
        lengt = len(self.p.xml)
        self.txtPayloadSize.setText(str(lengt))
        self.evalEmbed()

    def saveImage(self):
        print("OpeiOP")
        filePath, _ = QFileDialog.getSaveFileName(self, caption='Save file ...')

        if not filePath:
            return

        e = self.q.embedPayload(payload=self.p, override=self.chkOverride.isChecked())

        imsave(filePath, e)
        print(filePath)

    def cleanImage(self):
        print("clean")
        clnimg = self.q2.clean()
        imsave(self.filePath, clnimg)
        pixmap = QtGui.QPixmap(self.filePath)
        pixmap = pixmap.scaled(358, 278, QtCore.Qt.KeepAspectRatio)
        pixItem = QtGui.QGraphicsPixmapItem(pixmap)
        scn = QtGui.QGraphicsScene()
        scn.addItem(pixItem)
        self.viewCarrier2.setScene(scn)
        img = imread(self.filePath)
        test = Carrier(img=img)
        if test.payloadExists():
            print("didnot work")
        self.btnExtract.setEnabled(False)
        self.btnClean.setEnabled(False)
        self.lblCarrierEmpty.setText(">>>>Carrier Empty<<<<")
        self.viewPayload2.setScene(QtGui.QGraphicsScene())



    def extractImage(self):
        print("extract")
        extimg = self.q2.extractPayload()
        tempsavepath = self.filePath.split(".")[0] + "ext." + self.filePath.split(".")[1]
        print(tempsavepath)
        imsave(tempsavepath, extimg.img)
        pixmap = QtGui.QPixmap(tempsavepath)
        pixmap = pixmap.scaled(358, 278, QtCore.Qt.KeepAspectRatio)
        pixItem = QtGui.QGraphicsPixmapItem(pixmap)
        scn = QtGui.QGraphicsScene()
        scn.addItem(pixItem)
        self.viewPayload2.setScene(scn)
        os.remove(tempsavepath)



if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = SteganographyConsumer()
    currentForm.show()
    currentApp.exec_()
