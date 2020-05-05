from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

import design
import db

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.seats("BA1476"))

    def seats(self, number):
        self.label.setText(str(db.select_free_seats(number)))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.setWindowTitle('App')
    # window.setGeometry(100, 100, 800, 400)
    # window.setFixedSize(800, 600)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()