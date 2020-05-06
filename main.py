from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

import design
import db

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.hide1())
        # self.pushButton_2.clicked.connect(lambda: self.show1())
        # print(self.verticalFrame_2.frameGeometry().height())
        # self.statusBar().hide()

        # self.listWidget.addItem("hdsgfadsfjkaskajdhfsdakjhdvakvfdhvfsdajv hjsdav fv fsdajksf dvhj afsdvhj fsakj")
        # # self.listWidget.setMinimumWidth(self.listWidget.sizeHintForColumn(0) + 30)
        # self.listWidget.setMinimumWidth(400)
        # for i in range(50):
        #     self.listWidget.addItem(str(i))

    def select_free_seats(self):
        self.label.setText(str(db.select_free_seats(str(self.line.text()))))

    def all_baggage_cost(self):
        self.label.setText(str(db.all_baggage_cost(str(self.line.text()))))

    def hide1(self):
        self.frame.hide()
    
    def show1(self):
        self.frame.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = ExampleApp()
    window.setWindowTitle('App')
    # window.statusBar().hide()
    # window.setGeometry(100, 100, 800, 400)
    window.setFixedSize(800, 500)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()