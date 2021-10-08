from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget
from calctest import Ui_MainWindow

import time

class Math_calcul:
    def plus(a, b):
        return float(a) + float(b)
        
    def minus(a, b):
        return float(a) - float(b)

    def division(a, b):
        return float(a) / float(b)

    def multiplication(a, b):
        return float(a) * float(b)


class Window(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        self.s = False
        self.attempt = True
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.add_functions()

        # self.btn_zero.hide()

    def add_functions(self):
        self.btn_zero.clicked.connect(lambda: self.write_namber(self.btn_zero.text(), check = 0))
        self.btn_1.clicked.connect(lambda: self.write_namber(self.btn_1.text(), check = 0))
        self.btn_2.clicked.connect(lambda: self.write_namber(self.btn_2.text(), check = 0))
        self.btn_3.clicked.connect(lambda: self.write_namber(self.btn_3.text(), check = 0))
        self.btn_4.clicked.connect(lambda: self.write_namber(self.btn_4.text(), check = 0))
        self.btn_5.clicked.connect(lambda: self.write_namber(self.btn_5.text(), check = 0))
        self.btn_6.clicked.connect(lambda: self.write_namber(self.btn_6.text(), check = 0))
        self.btn_7.clicked.connect(lambda: self.write_namber(self.btn_7.text(), check = 0))
        self.btn_8.clicked.connect(lambda: self.write_namber(self.btn_8.text(), check = 0))
        self.btn_9.clicked.connect(lambda: self.write_namber(self.btn_9.text(), check = 0))
        self.btn_plus.clicked.connect(lambda: self.write_namber(self.btn_plus.text(), check = 1))
        self.btn_minus.clicked.connect(lambda: self.write_namber(self.btn_minus.text(), check = 1))
        self.btn_division.clicked.connect(lambda: self.write_namber(self.btn_division.text(), check = 1))
        self.btn_multiplication.clicked.connect(lambda: self.write_namber(self.btn_multiplication.text(), check = 1))
        self.btn_equ.clicked.connect(self.results)
        self.btn_clear.clicked.connect(lambda: self.delete())
        self.btn_backspace.clicked.connect(lambda:self.del_number())
    
    def event(self, e):
        if e.type() == QtCore.QEvent.KeyPress:
            if self.label.text() == " ERROR":
                self.label.setText(" ")
            if 48 <= e.key() <= 57:
                self.write_namber(e.text(), check = 0)
            elif e.key() == 47 or e.key() == 42 or e.key() == 45 or e.key() == 43:
                self.write_namber((" " + e.text() + " "), check = 1)
            elif e.key() == 16777219:
                self.del_number()
            elif e.key() == 16777221:
                self.results()
            print("Код:", e.key(), ", текст:", e.text())
        elif e.type() == QtCore.QEvent.Close:
            print("Вы закрыли окно")
        # if self.add_functions:
            # if self.label.text() == " ERROR":
            #     self.label.setText(" ")
            
        # elif e.type() == QtCore.QEvent.MouseButtonPress:
        #     if self.label.text() == " ERROR":
        #         self.label.setText(" ")
        #         print("*----------------------------")
        return QWidget.event(self, e)

    def del_number(self):
        lenth = len(self.label.text())
        text = self.label.text()
        chek = text[lenth - 1: lenth]
        if lenth > 3 and chek in " ":
            text = text[:lenth - 3]  
            self.s = True
        else:
            if lenth <= 1:
                pass
            else:
                text = text[:lenth - 1]
                self.s = True
        self.label.setText(text)


    def write_namber(self, number, check):
        if check == 0:
            self.s = True
        if self.s:
            if self.label.text() == " 0":
                self.label.setText(" "  + number)
            else:
                self.label.setText(self.label.text() + number)
            if check == 1:
                self.s = False

    def delete(self):
        self.label.setText(" ")
        if self.attempt:
            self.t1 = time.perf_counter()
            self.attempt = not self.attempt
        else:
            t2 = time.perf_counter()
            if t2 - self.t1 < 1:
                self.textBrowser.clear()
            self.attempt = not self.attempt
    def results(self):
        res = self.myeval(self.label.text())
        self.textBrowser.append(self.label.text() + " = " + str(res))
        self.label.setText(" " + str(res))


    def myeval(self, number):
        perem1 = []
        a = [] 
        count = 0
        symvls = {"/": "/", 
                "*": "*",
                "+":'+',
                "-": "-"}
        symvls1 = []
        a = (number.split())
        for i in a:
            if i in symvls:
                symvls1.append(i)
                count += 1 
            elif i.isdigit :
                perem1.append(i)

        for i in range(0, count):

            if "*" in symvls1 or "/" in symvls1:
                if "/" in symvls1:
                    ind = symvls1.index("/")
                    res1 = Math_calcul.division(perem1[ind], perem1[ind + 1])
                    symvls1.pop(ind)
                    perem1.pop(ind)
                    perem1[ind] = res1
                    res1 = 0
                else:
                    ind = symvls1.index("*")
                    res1 = Math_calcul.multiplication(perem1[ind], perem1[ind + 1])
                    symvls1.pop(ind)
                    perem1.pop(ind)
                    perem1[ind] = res1
                    res1 = 0

            elif "+" in symvls1 :
                ind = symvls1.index("+")
                res1 = Math_calcul.plus(perem1[ind], perem1[ind + 1])
                symvls1.pop(ind)
                perem1.pop(ind)
                perem1[ind] = res1
                res1 = 0
            elif "-" in symvls1 :
                ind = symvls1.index("-")
                res1 = Math_calcul.minus(perem1[ind], perem1[ind + 1])
                symvls1.pop(ind)
                perem1.pop(ind)
                perem1[ind] = res1
                res1 = 0
        return int(perem1[0]) if perem1[0].is_integer() else round(perem1[0], 12)


