from PyQt5 import QtWidgets
import sys
from newcal import Ui_MainWindow

class Window(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        self.s = False
        self.attempt = True
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = Window()

    application.show()
    sys.exit(app.exec_())