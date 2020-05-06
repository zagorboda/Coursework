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
        MainWindow.resize(800, 500)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color:white;")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 100, 105, 23))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QLineEdit(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(330, 50, 133, 20))
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 50, 47, 13))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 80, 460))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("border-color:white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 81, 461))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalLayoutWidget.sizePolicy().hasHeightForWidth())
        self.verticalLayoutWidget.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget.setStyleSheet("")
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("margin:10px;\n"
"border-radius: 15px;\n"
"background-color:#42ecf5;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("margin:10px;\n"
"border-radius: 15px;\n"
"background-color:#42ecf5;\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("margin:10px;\n"
"border-radius: 15px;\n"
"background-color:#42ecf5;\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setStyleSheet("margin:10px;\n"
"border-radius: 15px;\n"
"background-color:#42ecf5;\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_3.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setStyleSheet("margin:10px;\n"
"border-radius: 15px;\n"
"background-color:#42ecf5;\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_3.addWidget(self.pushButton_11)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFirst = QtWidgets.QMenu(self.menubar)
        self.menuFirst.setObjectName("menuFirst")
        self.menuSecond = QtWidgets.QMenu(self.menubar)
        self.menuSecond.setObjectName("menuSecond")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action12 = QtWidgets.QAction(MainWindow)
        self.action12.setObjectName("action12")
        self.action12_2 = QtWidgets.QAction(MainWindow)
        self.action12_2.setObjectName("action12_2")
        self.menuFirst.addAction(self.action1)
        self.menuFirst.addAction(self.action2)
        self.menuSecond.addAction(self.action12)
        self.menuSecond.addAction(self.action12_2)
        self.menubar.addAction(self.menuFirst.menuAction())
        self.menubar.addAction(self.menuSecond.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Get free seats"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "2"))
        self.pushButton_4.setText(_translate("MainWindow", "3"))
        self.pushButton_10.setText(_translate("MainWindow", "4"))
        self.pushButton_11.setText(_translate("MainWindow", "5"))
        self.menuFirst.setTitle(_translate("MainWindow", "First"))
        self.menuSecond.setTitle(_translate("MainWindow", "Second"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.action2.setText(_translate("MainWindow", "2"))
        self.action12.setText(_translate("MainWindow", "11"))
        self.action12_2.setText(_translate("MainWindow", "12"))
