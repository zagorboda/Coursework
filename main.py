from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

import design
import db

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.find_info_number_btn.clicked.connect(self.select_info_by_number)
        self.find_info_direction_btn.clicked.connect(self.select_info_by_direction)
        self.find_info_date_btn.clicked.connect(self.select_info_by_date)

        self.get_info.clicked.connect(lambda: self.show_(0))
        self.additional_info.clicked.connect(lambda: self.show_(1))


        self.get_number_of_free_seats_btn.clicked.connect(self.select_free_seats)
        self.get_baggage_sum_btn.clicked.connect(self.select_baggage_sum)



        
        # self.tabWidget.setStyleSheet("""
        # QTabBar::tab {
        #     //margin-left:10px;
        #     color:red;
        #     }
        # """)

        # self.stackedWidget.setCurrentIndex(6)

        # self.statusbar.showMessage("123")
        # self.statusBar().hide()

        # self.listWidget.addItem("hdsgfadsfjkaskajdhfsdakjhdvakvfdhvfsdajv hjsdav fv fsdajksf dvhj afsdvhj fsakj")
        # # self.listWidget.setMinimumWidth(self.listWidget.sizeHintForColumn(0) + 30)
        # self.listWidget.setMinimumWidth(400)
        # for i in range(50):
        #     self.listWidget.addItem(str(i))

    def show_(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def select_free_seats(self):
        res = db.select_free_seats(str(self.free_seats_number_input.text()))
        if res == -1:
            self.free_seats_number_input_error.setText("No such flight")
        else:
            self.free_seats_number_input_error.setText("")
            self.number_of_free_seats.setText(str(res))

    def select_baggage_sum(self):
        res = db.all_baggage_cost(str(self.baggage_sum_number_input.text()))
        if res == -1:
            self.baggage_sum_number_input_error.setText("No such flight")
        else:
            self.baggage_sum_number_input_error.setText("")
            self.baggage_sum.setText(str(res))

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
    
    def select_info_by_date(self):
        results = db.get_flight_info_by_date(str(self.date_input.text()))
        if results == -1:
            self.date_input_error.setText("No such flight")
        else:
            self.flight_info_by_date_list.clear()
            self.date_input_error.setText("")
            for res in results:
                self.flight_info_by_date_list.addItem("Number : {}".format(res[0]))
                self.flight_info_by_date_list.addItem("Flight from {} to {}".format(res[1].split('|')[0], res[1].split('|')[1]))
                self.flight_info_by_date_list.addItem("All seats : {}".format(res[2]))
                self.flight_info_by_date_list.addItem("Free seats : {}".format(res[3]))
                self.flight_info_by_date_list.addItem("")

    def all_baggage_cost(self):
        self.label.setText(str(db.all_baggage_cost(str(self.line.text()))))

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