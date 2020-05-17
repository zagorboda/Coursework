# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 500)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color:white;")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menu = QtWidgets.QFrame(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(0, 0, 131, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setStyleSheet("border-color:white;")
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.change_info = QtWidgets.QPushButton(self.menu)
        self.change_info.setGeometry(QtCore.QRect(0, 100, 130, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_info.sizePolicy().hasHeightForWidth())
        self.change_info.setSizePolicy(sizePolicy)
        self.change_info.setStyleSheet("margin:10px;\n"
"border-radius: 15px;\n"
"background-color:#42ecf5;\n"
"")
        self.change_info.setObjectName("change_info")
        self.get_info = QtWidgets.QPushButton(self.menu)
        self.get_info.setGeometry(QtCore.QRect(0, 20, 130, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_info.sizePolicy().hasHeightForWidth())
        self.get_info.setSizePolicy(sizePolicy)
        self.get_info.setStyleSheet("margin:10px;\n"
"border-radius: 15px;\n"
"background-color:#42ecf5;\n"
"")
        self.get_info.setObjectName("get_info")
        self.login = QtWidgets.QPushButton(self.menu)
        self.login.setGeometry(QtCore.QRect(20, 410, 90, 50))
        self.login.setStyleSheet("margin:10px;\n"
"border-radius: 15px;\n"
"background-color:#42ecf5;\n"
"")
        self.login.setObjectName("login")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setGeometry(QtCore.QRect(130, 0, 671, 481))
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.groupBox = QtWidgets.QGroupBox(self.frame_1)
        self.groupBox.setGeometry(QtCore.QRect(130, 50, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("border:0px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radio_number = QtWidgets.QRadioButton(self.groupBox)
        self.radio_number.setGeometry(QtCore.QRect(10, 30, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_number.setFont(font)
        self.radio_number.setObjectName("radio_number")
        self.radio_direction = QtWidgets.QRadioButton(self.groupBox)
        self.radio_direction.setGeometry(QtCore.QRect(140, 30, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_direction.setFont(font)
        self.radio_direction.setObjectName("radio_direction")
        self.radion_date = QtWidgets.QRadioButton(self.groupBox)
        self.radion_date.setGeometry(QtCore.QRect(270, 30, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radion_date.setFont(font)
        self.radion_date.setObjectName("radion_date")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, -10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.get_info_number = QtWidgets.QFrame(self.frame_1)
        self.get_info_number.setGeometry(QtCore.QRect(9, 140, 641, 341))
        self.get_info_number.setStyleSheet("border:0px;")
        self.get_info_number.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.get_info_number.setFrameShadow(QtWidgets.QFrame.Raised)
        self.get_info_number.setObjectName("get_info_number")
        self.label_2 = QtWidgets.QLabel(self.get_info_number)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.enter_number = QtWidgets.QLineEdit(self.get_info_number)
        self.enter_number.setGeometry(QtCore.QRect(180, 20, 113, 20))
        self.enter_number.setStyleSheet("border:1px solid;")
        self.enter_number.setObjectName("enter_number")
        self.find_info_number_btn = QtWidgets.QPushButton(self.get_info_number)
        self.find_info_number_btn.setGeometry(QtCore.QRect(30, 60, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.find_info_number_btn.setFont(font)
        self.find_info_number_btn.setStyleSheet("border:2px solid teal;\n"
"border-radius:5px;")
        self.find_info_number_btn.setObjectName("find_info_number_btn")
        self.flight_info_by_number_list = QtWidgets.QListWidget(self.get_info_number)
        self.flight_info_by_number_list.setGeometry(QtCore.QRect(30, 100, 601, 192))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.flight_info_by_number_list.setFont(font)
        self.flight_info_by_number_list.setStyleSheet("")
        self.flight_info_by_number_list.setObjectName("flight_info_by_number_list")
        self.find_number_error = QtWidgets.QLabel(self.get_info_number)
        self.find_number_error.setGeometry(QtCore.QRect(320, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.find_number_error.setFont(font)
        self.find_number_error.setStyleSheet("color:orange;")
        self.find_number_error.setText("")
        self.find_number_error.setObjectName("find_number_error")
        self.get_info_direction = QtWidgets.QFrame(self.get_info_number)
        self.get_info_direction.setGeometry(QtCore.QRect(0, 0, 641, 341))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.get_info_direction.setFont(font)
        self.get_info_direction.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.get_info_direction.setFrameShadow(QtWidgets.QFrame.Raised)
        self.get_info_direction.setObjectName("get_info_direction")
        self.label_3 = QtWidgets.QLabel(self.get_info_direction)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.departure_input = QtWidgets.QLineEdit(self.get_info_direction)
        self.departure_input.setGeometry(QtCore.QRect(100, 30, 113, 20))
        self.departure_input.setStyleSheet("border:1px solid;")
        self.departure_input.setObjectName("departure_input")
        self.label_4 = QtWidgets.QLabel(self.get_info_direction)
        self.label_4.setGeometry(QtCore.QRect(270, 30, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.arrival_input = QtWidgets.QLineEdit(self.get_info_direction)
        self.arrival_input.setGeometry(QtCore.QRect(330, 30, 113, 20))
        self.arrival_input.setStyleSheet("border:1px solid;")
        self.arrival_input.setObjectName("arrival_input")
        self.find_info_direction_btn = QtWidgets.QPushButton(self.get_info_direction)
        self.find_info_direction_btn.setGeometry(QtCore.QRect(20, 70, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.find_info_direction_btn.setFont(font)
        self.find_info_direction_btn.setStyleSheet("border:2px solid teal;\n"
"border-radius:5px;")
        self.find_info_direction_btn.setObjectName("find_info_direction_btn")
        self.flight_info_by_direction_list = QtWidgets.QListWidget(self.get_info_direction)
        self.flight_info_by_direction_list.setGeometry(QtCore.QRect(20, 110, 601, 192))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.flight_info_by_direction_list.setFont(font)
        self.flight_info_by_direction_list.setObjectName("flight_info_by_direction_list")
        self.find_direction_error = QtWidgets.QLabel(self.get_info_direction)
        self.find_direction_error.setGeometry(QtCore.QRect(470, 30, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.find_direction_error.setFont(font)
        self.find_direction_error.setStyleSheet("color:orange;")
        self.find_direction_error.setText("")
        self.find_direction_error.setObjectName("find_direction_error")
        self.frame_1.raise_()
        self.menu.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action12 = QtWidgets.QAction(MainWindow)
        self.action12.setObjectName("action12")
        self.action12_2 = QtWidgets.QAction(MainWindow)
        self.action12_2.setObjectName("action12_2")
        self.action1_1 = QtWidgets.QAction(MainWindow)
        self.action1_1.setObjectName("action1_1")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.change_info.setText(_translate("MainWindow", "Cahnge flight info"))
        self.get_info.setText(_translate("MainWindow", "Get flight info"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.radio_number.setText(_translate("MainWindow", "Number"))
        self.radio_direction.setText(_translate("MainWindow", "Direction"))
        self.radion_date.setText(_translate("MainWindow", "Date"))
        self.label.setText(_translate("MainWindow", "Find flights information by"))
        self.label_2.setText(_translate("MainWindow", "Enter flight number"))
        self.find_info_number_btn.setText(_translate("MainWindow", "Find"))
        self.label_3.setText(_translate("MainWindow", "Departure"))
        self.label_4.setText(_translate("MainWindow", "Arrival"))
        self.find_info_direction_btn.setText(_translate("MainWindow", "Find"))
        self.action2.setText(_translate("MainWindow", "2"))
        self.action12.setText(_translate("MainWindow", "11"))
        self.action12_2.setText(_translate("MainWindow", "12"))
        self.action1_1.setText(_translate("MainWindow", "1.1"))
