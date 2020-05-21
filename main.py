# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets
import sys

import design
import db

import datetime

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('airplane.svg'))

        self.logged = True #---------------------------------------------------------------#

        self.find_info_number_btn.clicked.connect(self.select_info_by_number)
        self.find_info_direction_btn.clicked.connect(self.select_info_by_direction)
        self.find_info_date_btn.clicked.connect(self.select_info_by_date)

        self.get_info.clicked.connect(lambda: self.show_(0))
        self.additional_info.clicked.connect(lambda: self.show_(1))
        self.view_info_admin.clicked.connect(lambda: self.show_(2))
        self.insert_info.clicked.connect(lambda: self.show_(3))
        self.login.clicked.connect(lambda: self.show_(4))
        self.log_in_btn.clicked.connect(self.log_in)

        self.get_number_of_free_seats_btn.clicked.connect(self.select_free_seats)
        self.get_baggage_sum_btn.clicked.connect(self.select_baggage_sum)
        
        self.label_12.hide()
        self.label_13.hide()

        self.find_info_surname_btn.clicked.connect(self.show_info_by_surname)
        self.find_info_direction_btn_2.clicked.connect(self.select_info_by_number_admin)

        self.apply_insert_flight_info.clicked.connect(self.insert_fligh_info)
        self.apply_insert_passenger_info.clicked.connect(self.insert_passenger_info)

    def log_in(self):
        login = self.login_input.text()
        password = self.password_input.text()
        if login == "123" and password == "123":
            self.logged = True
            self.statusbar.showMessage("You are logged in")
            self.login_error.setText("")
            self.login_input.clear()
            self.password_input.clear()
        else:
            self.login_error.setText("Incorrect login or password")

    def show_(self, index):
        if index == 0 or index == 1 or index == 4:
            self.stackedWidget.setCurrentIndex(index)
        elif self.logged is True:
            self.stackedWidget.setCurrentIndex(index)

    def select_free_seats(self):
        res = db.select_free_seats(str(self.free_seats_number_input.text()))
        if res == -1:
            self.free_seats_number_input_error.setText("No such flight")
        else:
            self.label_12.show()
            self.free_seats_number_input_error.setText("")
            self.number_of_free_seats.setText(str(res))

    def select_baggage_sum(self):
        res = db.all_baggage_cost(str(self.baggage_sum_number_input.text()))
        if res == -1:
            self.baggage_sum_number_input_error.setText("No such flight")
        else:
            self.label_13.show()
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

    def show_info_by_surname(self):
        result = db.get_flight_info_by_surname(str(self.surname_input.text()))
        if result == -1:
            self.find_surname_error.setText("No such passenger")
        else:
            self.flight_info_by_surname_list.clear()
            self.find_surname_error.setText("")
            for row in result:
                res = row[0]
                self.flight_info_by_surname_list.addItem("Number : {}".format(res[0]))
                self.flight_info_by_surname_list.addItem("Flight from {} to {}".format(res[1].split('|')[0], res[1].split('|')[1]))
                self.flight_info_by_surname_list.addItem("All seats : {}".format(res[2]))
                self.flight_info_by_surname_list.addItem("Free seats : {}".format(res[3]))
                self.flight_info_by_surname_list.addItem("Date : {}".format(res[4]))
                self.flight_info_by_surname_list.addItem("")
    
    def select_info_by_number_admin(self):
        dest = self.departure_input_2.text()
        arr = self.arrival_input_2.text()
        result = db.get_short_flight_info_by_direction(str(dest + "|" + arr))
        if result == -1:
            self.find_direction_error_2.setText("No such direction")
        else:
            self.flight_info_by_direction_list_2.clear()
            self.find_direction_error_2.setText("")
            for i in range(len(result)):
                if (i+1)%3 == 0 and i!= 0:
                    for j in range(len(result[i])):
                        self.flight_info_by_direction_list_2.addItem("\t" + result[i][j][0])
                    self.flight_info_by_direction_list_2.addItem("\n\n")
                elif i%3 == 0:
                    self.flight_info_by_direction_list_2.addItem("Number : {}".format(result[i]))
                else:
                    self.flight_info_by_direction_list_2.addItem("Date : {}".format(result[i]))

    def insert_fligh_info(self):
        number_error = False
        departure_error = False
        arrival_error = False
        seats_error = False
        date_error = False

        number = self.insert_flight_info_number_input.text()
        departure = self.insert_flight_info_departure_input.text()
        arrival = self.insert_flight_info_arrival_input.text()
        all_seats = self.insert_flight_info_all_seats_input.text()
        date = self.insert_flight_info_date_input.text()

        if len(number) == 0:
            number_error = True
        
        if len(departure) == 0:
            departure_error = True
        
        if len(arrival) == 0:
            arrival_error = True

        try:
            int(all_seats)
        except ValueError:
            seats_error = True
        else:
            if int(all_seats) <= 0:
                seats_error = True
            else:
                seats_error = False
 
        if date.count(".") == 2:
            day,month,year = date.split(".")

            try:
                datetime.datetime(int(year),int(month),int(day))
            except ValueError :
                date_error = True
        else:
            date_error = True

        if number_error is True:
            self.number_error.setText("Incorrect input")
        else:
            self.number_error.setText("")

        if departure_error is True:
            self.departure_error.setText("Incorrect input")
        else:
            self.departure_error.setText("")

        if arrival_error is True:
            self.arrival_error.setText("Incorrect input")
        else:
            self.arrival_error.setText("")

        if seats_error is True:
            self.amount_of_seats_error.setText("Incorrect input")
        else:
            self.amount_of_seats_error.setText("")

        if date_error is True:
            self.date_insert_error.setText("Incorrect input")
        else:
            self.date_insert_error.setText("")
        
        

        if number_error is False and departure_error is False and arrival_error is False and seats_error is False and date_error is False:
            direction = departure + "|" + arrival
            res = db.insert_flight([number, direction, all_seats, all_seats, date])
            if res == 0:
                self.insert_error.setText("Flight successfully added")
            if res == -1:
                self.insert_error.setText("Flight with this number alredy exist")
            self.insert_flight_info_number_input.clear()
            self.insert_flight_info_departure_input.clear()
            self.insert_flight_info_arrival_input.clear()
            self.insert_flight_info_all_seats_input.clear()
            self.insert_flight_info_date_input.clear()
        
    def insert_passenger_info(self):
        surname = self.insert_passenger_info_surname_input.text()
        flight_number = self.insert_passenger_info_number_input.text()
        flight_class = str(self.insert_passenger_info_class_combo.currentText())
        baggage_cost = self.insert_passenger_info_baggage_input.text()
        ticket_cost = self.insert_passenger_info_cost_input.text()

        surname_error = False
        number_error = False
        baggage_error = False
        ticket_error = False

        if len(surname) == 0:
            surname_error = True
        
        if len(flight_number) == 0:
            number_error = True
        
        if len(baggage_cost) == 0:
            baggage_error = True

        if len(ticket_cost) == 0:
            ticket_error = True
        
        try:
            float(baggage_cost)
        except ValueError:
            baggage_error = True
        else:
            if float(baggage_cost) < 0:
                baggage_error = True
            else:
                baggage_error = False
        
        try:
            float(ticket_cost)
        except ValueError:
            ticket_error = True
        else:
            if float(ticket_cost) <= 0:
                ticket_error = True
            else:
                ticket_error = False
        
        numbers = db.get_all_flight_numbers()

        if flight_number not in numbers:
            number_error = True

        if surname_error is True:
            self.passenger_surname_input_error.setText("Incorrect input")
        else:
            self.passenger_surname_input_error.setText("")

        if number_error is True:
            self.passenger_flight_input_error.setText("No such flight")
        else:
            self.passenger_flight_input_error.setText("")

        if baggage_error is True:
            self.baggage_cost_input_error.setText("Incorrect input")
        else:
            self.baggage_cost_input_error.setText("")

        if ticket_error is True:
            self.ticket_cost_input_error.setText("Incorrect input")
        else:
            self.ticket_cost_input_error.setText("")
        
        if surname_error == False and number_error == False and baggage_error == False and ticket_error == False:
            free_seats = db.select_free_seats(flight_number)
            if free_seats <= 0:
                self.insert_passenger_error.setText("Flight doesn't have free seats")
            else:
                db.insert_passenger([surname, flight_number, flight_class, baggage_cost, ticket_cost])
                self.insert_passenger_error.setText("Passenger info successfully added")
                self.insert_passenger_info_surname_input.clear()
                self.insert_passenger_info_baggage_input.clear()
                self.insert_passenger_info_cost_input.clear()
                db.decrement_free_seats(flight_number)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = ExampleApp()
    window.setWindowTitle('Airport')
    window.setFixedSize(800, 500)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
    