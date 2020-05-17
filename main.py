from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

import design
import db

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.change_info.clicked.connect(self.show1)

        self.radio_number.toggled.connect(self.onClicked)
        self.radio_direction.toggled.connect(self.onClicked)
        self.radio_number.setChecked(True)

        self.get_info_direction.hide()

        self.find_info_number_btn.clicked.connect(self.select_info_by_number)
        self.find_info_direction_btn.clicked.connect(self.select_info_by_direction)

        # self.statusbar.showMessage("123")
        # self.statusBar().hide()

        # self.listWidget.addItem("hdsgfadsfjkaskajdhfsdakjhdvakvfdhvfsdajv hjsdav fv fsdajksf dvhj afsdvhj fsakj")
        # # self.listWidget.setMinimumWidth(self.listWidget.sizeHintForColumn(0) + 30)
        # self.listWidget.setMinimumWidth(400)
        # for i in range(50):
        #     self.listWidget.addItem(str(i))

    def onClicked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            if radioBtn.text() == "Number":
                self.get_info_number.show()
                self.get_info_direction.hide()
            if radioBtn.text() == "Direction":
                self.get_info_direction.show()

    def select_free_seats(self):
        self.label.setText(str(db.select_free_seats(str(self.line.text()))))

    def select_info_by_number(self):
        res = db.get_flight_info_by_number(str(self.enter_number.text()))
        if res == -1:
            self.find_number_error.setText("No such flight")
        else:
            res = res[0]
            self.flight_info_by_number_list.clear()
            self.find_number_error.setText("")
            self.flight_info_by_number_list.addItem("Flight from {} to {}".format(res[1].split('|')[0], res[1].split('|')[1]))
            self.flight_info_by_number_list.addItem("All seats : {}".format(res[2]))
            self.flight_info_by_number_list.addItem("Free seats : {}".format(res[3]))
            self.flight_info_by_number_list.addItem("Date : {}".format(res[4]))

    def select_info_by_direction(self):
        dest = self.departure_input.text()
        arr = self.arrival_input.text()
        results = db.get_flight_info_by_direction(str(dest + "|" + arr))
        if results == -1:
            self.find_direction_error.setText("No such flight")
        else:
            self.flight_info_by_direction_list.clear()
            self.find_direction_error.setText("")
            for res in results:
                self.flight_info_by_direction_list.addItem("Number : {}".format(res[0]))
                self.flight_info_by_direction_list.addItem("All seats : {}".format(res[2]))
                self.flight_info_by_direction_list.addItem("Free seats : {}".format(res[3]))
                self.flight_info_by_direction_list.addItem("Date : {}".format(res[4]))
                self.flight_info_by_direction_list.addItem("")

    def all_baggage_cost(self):
        self.label.setText(str(db.all_baggage_cost(str(self.line.text()))))

    def hide1(self):
        self.frame_2.hide()
    
    def show1(self):
        self.frame_1.raise_()

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