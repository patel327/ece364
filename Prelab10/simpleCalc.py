#! /usr/bin/env python3.4

# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *

prevNum = 0
start = True
oper = ""
Calc = True
save = 0
res = 0

class CalculatorConsumer(QMainWindow, Ui_Calculator):

    def __init__(self, parent=None):
        super(CalculatorConsumer, self).__init__(parent)
        self.setupUi(self)
        self.btn0.clicked.connect(self.Numbers)
        self.btn1.clicked.connect(self.Numbers)
        self.btn2.clicked.connect(self.Numbers)
        self.btn3.clicked.connect(self.Numbers)
        self.btn4.clicked.connect(self.Numbers)
        self.btn5.clicked.connect(self.Numbers)
        self.btn6.clicked.connect(self.Numbers)
        self.btn7.clicked.connect(self.Numbers)
        self.btn8.clicked.connect(self.Numbers)
        self.btn9.clicked.connect(self.Numbers)
        self.btnDot.clicked.connect(self.Numbers)

        self.btnPlus.clicked.connect(self.Op)
        self.btnDivide.clicked.connect(self.Op)
        self.btnMinus.clicked.connect(self.Op)
        self.btnMultiply.clicked.connect(self.Op)

        self.btnEqual.clicked.connect(self.Eq)

        self.btnClear.clicked.connect(self.tClr)
        self.txtDisplay.setText("0")


    def tClr(self):
        global start
        global Calc
        global save
        save = 0
        start = True
        Calc = True
        self.txtDisplay.setText("0")

    def Clr(self):
        global start
        global Calc
        start = True

        try:
            self.txtDisplay.setText("0")
        except:
            pass

    def Numbers(self):
        global start

        if int(self.txtDisplay.text().split(".")[0]) // 100000000000 == 0:
            if start != True:
                self.txtDisplay.setText( self.txtDisplay.text() + self.sender().text())
            else:
                self.txtDisplay.setText(self.sender().text())
                start=False
        else:
            #self.txtDisplay.setText(self.txtDisplay.text()[1:] + self.sender().text())
            pass

        #self.evalThousands(float(self.txtDisplay.text().replace(",","")))


    def evalThousands(self, numbers):
        if self.chkSeparator.isChecked():
            self.txtDisplay.setText(('{0:,.' + str(self.cboDecimal.currentIndex()) + 'f}').format(numbers))
        else:
            self.txtDisplay.setText(('{0:.' + str(self.cboDecimal.currentIndex()) + 'f}').format(numbers))


    def Op(self):
        global prevNum
        global oper
        global Calc
        global save

        if save != 0:
            Calc = True
            self.Eq()

        if save == 0:
            Calc = True
            save =1
            prevNum = self.txtDisplay.text().replace(",", "")
            print(prevNum)
        oper = self.sender().text()
        self.Clr()




    def Eq(self):
        global prevNum
        global oper
        global save
        global res
        global Calc
        #prevNum = self.txtDisplay.text().replace(",", "")
        print("ineq")
        if Calc == False:
            save = 0
        if oper == "+":
            result = float(prevNum) + float(self.txtDisplay.text().replace(",",""))
            res = result
            self.txtDisplay.setText(str(result))
            prevNum = result
            print(prevNum)

        if oper == "-":
            result = float(prevNum) - float(self.txtDisplay.text().replace(",",""))
            self.txtDisplay.setText(str(result))
            prevNum = result

        if oper == "x":
            result = float(prevNum) * float(self.txtDisplay.text().replace(",",""))
            self.txtDisplay.setText(str(result))
            prevNum = result

        if oper == "/":
            result = 0
            try:
                result = float(prevNum) / float(self.txtDisplay.text().replace(",",""))
                self.txtDisplay.setText(str(result))
            except:
                self.txtDisplay.setText("ERROR")
            prevNum = result
        print(prevNum)
        try:
            self.evalThousands(float(self.txtDisplay.text().replace(",","")))
        except:
            pass
        Calc = False
        oper = ""



currentApp = QApplication(sys.argv)
currentForm = CalculatorConsumer()

currentForm.show()
currentApp.exec_()