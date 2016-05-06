import sys

from PySide.QtGui import *
from BasicUI import *
import re

class Consumer(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.clearButton.clicked.connect(self.clr)
        self.saveToTargetButton.clicked.connect(self.valid)
        self.addressLineEdit.textChanged.connect(self.data)
        self.firstNameLineEdit.textChanged.connect(self.data)
        self.lastNameLineEdit.textChanged.connect(self.data)
        #self.addressLineEdit.textChanged.connect(self.data)
        self.cityLineEdit.textChanged.connect(self.data)
        self.stateLineEdit.textChanged.connect(self.data)
        self.zipLineEdit.textChanged.connect(self.data)
        self.emailLineEdit.textChanged.connect(self.data)
        self.loadButton.clicked.connect(self.loadData)




    def data(self):
        self.saveToTargetButton.setEnabled(True)
        self.loadButton.setEnabled(False)

    def valid(self):

        if self.stateLineEdit.text() not in self.states:
            self.errorInfoLabel.setText("Error: Invalid State")
        elif not self.zipLineEdit.text().isdigit():
            self.errorInfoLabel.setText("Error:Invalid zip")
        elif int(self.zipLineEdit.text()) > 99999 or int(self.zipLineEdit.text()) < 10000:
                self.errorInfoLabel.setText("Error: Invalid Zip")
        elif not re.search(r"\w+@\w+\.\w+", self.emailLineEdit.text()):
            self.errorInfoLabel.setText("Error: Invalid Email")
        elif not self.addressLineEdit.text() or not self.firstNameLineEdit.text() or not self.lastNameLineEdit.text() or not self.stateLineEdit.text() or not self.cityLineEdit.text() or not self.zipLineEdit.text() or not self.emailLineEdit.text():
            self.errorInfoLabel.setText("Error: One or more Entries not populated")
        else:
            self.errorInfoLabel.setText("")
            with open("target.xml", "w") as f:
                f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                f.write('<user>\n')
                f.write('\t<FirstName>' + self.firstNameLineEdit.text() + '</FirstName>\n')
                f.write('\t<LastName>' + self.lastNameLineEdit.text() + '</LastName>\n')
                f.write('\t<Address>' + self.addressLineEdit.text() + '</Address>\n')
                f.write('\t<City>' + self.cityLineEdit.text() + '</City>\n')
                f.write('\t<State>' + self.stateLineEdit.text() + '</State>\n')
                f.write('\t<ZIP>' + self.zipLineEdit.text() + '</ZIP>\n')
                f.write('\t<Email>' + self.emailLineEdit.text() + '</Email>\n')
                f.write('</user>\n')



    def clr(self):
        self.firstNameLineEdit.setText("")
        self.lastNameLineEdit.setText("")
        self.addressLineEdit.setText("")
        self.cityLineEdit.setText("")
        self.stateLineEdit.setText("")
        self.zipLineEdit.setText("")
        self.emailLineEdit.setText("")
        self.saveToTargetButton.setEnabled(False)
        self.loadButton.setEnabled(True)
        self.errorInfoLabel.setText("")

    def loadDataFromFile(self, filePath):
        li = []
        with open(filePath, 'r') as f:
            lines = f.readlines()
            for line in lines[2:9]:
                y = line.split(">")
                data = y[1].split("<")[0]
                li.append(data)
        print(li)
        self.firstNameLineEdit.setText(li[0])
        self.lastNameLineEdit.setText(li[1])
        self.addressLineEdit.setText(li[2])
        self.cityLineEdit.setText(li[3])
        self.stateLineEdit.setText(li[4])
        self.zipLineEdit.setText(li[5])
        self.emailLineEdit.setText(li[6])

        pass

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
