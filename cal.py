from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget
from calctest import Ui_MainWindow
import sys
import time

class Window(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        self.s = False
        self.attempt = True
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.add_functions()

    def add_functions(self):
        self.ui.btn_zero.clicked.connect(lambda: self.write_namber(self.ui.btn_zero.text(), check = 0))
        self.ui.btn_1.clicked.connect(lambda: self.write_namber(self.ui.btn_1.text(), check = 0))
        self.ui.btn_2.clicked.connect(lambda: self.write_namber(self.ui.btn_2.text(), check = 0))
        self.ui.btn_3.clicked.connect(lambda: self.write_namber(self.ui.btn_3.text(), check = 0))
        self.ui.btn_4.clicked.connect(lambda: self.write_namber(self.ui.btn_4.text(), check = 0))
        self.ui.btn_5.clicked.connect(lambda: self.write_namber(self.ui.btn_5.text(), check = 0))
        self.ui.btn_6.clicked.connect(lambda: self.write_namber(self.ui.btn_6.text(), check = 0))
        self.ui.btn_7.clicked.connect(lambda: self.write_namber(self.ui.btn_7.text(), check = 0))
        self.ui.btn_8.clicked.connect(lambda: self.write_namber(self.ui.btn_8.text(), check = 0))
        self.ui.btn_9.clicked.connect(lambda: self.write_namber(self.ui.btn_9.text(), check = 0))
        self.ui.btn_plus.clicked.connect(lambda: self.write_namber(self.ui.btn_plus.text(), check = 1))
        self.ui.btn_minus.clicked.connect(lambda: self.write_namber(self.ui.btn_minus.text(), check = 1))
        self.ui.btn_division.clicked.connect(lambda: self.write_namber(self.ui.btn_division.text(), check = 1))
        self.ui.btn_multiplication.clicked.connect(lambda: self.write_namber(self.ui.btn_multiplication.text(), check = 1))
        self.ui.btn_equ.clicked.connect(self.results)
        self.ui.btn_clear.clicked.connect(lambda: self.delete())
        self.ui.btn_backspace.clicked.connect(lambda:self.del_number())
    
    def event(self, e):
        if e.type() == QtCore.QEvent.KeyPress:
            if self.ui.label.text() == " ERROR":
                self.ui.label.setText(" ")
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
            # if self.ui.label.text() == " ERROR":
            #     self.ui.label.setText(" ")
            
        # elif e.type() == QtCore.QEvent.MouseButtonPress:
        #     if self.ui.label.text() == " ERROR":
        #         self.ui.label.setText(" ")
        #         print("*----------------------------")
        return QWidget.event(self, e)

    def del_number(self):
        lenth = len(self.ui.label.text())
        text = self.ui.label.text()
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
        self.ui.label.setText(text)


    def write_namber(self, number, check):
        if check == 0:
            self.s = True
        if self.s:
            if self.ui.label.text() == " 0":
                self.ui.label.setText(" "  + number)
            else:
                self.ui.label.setText(self.ui.label.text() + number)
            if check == 1:
                self.s = False

    def delete(self):
        self.ui.label.setText(" ")
        if self.attempt:
            self.t1 = time.perf_counter()
            self.attempt = not self.attempt
        else:
            t2 = time.perf_counter()
            if t2 - self.t1 < 1:
                self.ui.textBrowser.clear()
            self.attempt = not self.attempt


    def results(self):
        if self.s == False:
            # time.sleep(2)
            self.ui.label.setText(" ERROR")
            # self.ui.label.setText(" ")
        else:
            res = eval(self.ui.label.text())
            self.ui.textBrowser.append(self.ui.label.text() + " = " + str(res))
            self.ui.label.setText(" " + str(res))

    # def evali(self, number):
    #     res = ""
    #     symvls = {"/": "/", "*": "*", "+" :"+"}
    #     for i in number:
    #         if i != "":
    #             res += i  

if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    application = Window()
    application.show()
    sys.exit(app.exec_())