# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, BorrowBook):
        BorrowBook.setObjectName("Borrow_book")
        BorrowBook.resize(665, 451)
        BorrowBook.setStyleSheet("background: black;\n"
"color: white")
        self.centralwidget = QtWidgets.QWidget(BorrowBook)
        self.centralwidget.setObjectName("centralwidget")
        self.UserIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.UserIDLabel.setGeometry(QtCore.QRect(60, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.UserIDLabel.setFont(font)
        self.UserIDLabel.setObjectName("UserIDLabel")
        self.BookCodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.BookCodeLabel.setGeometry(QtCore.QRect(60, 100, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BookCodeLabel.setFont(font)
        self.BookCodeLabel.setObjectName("BookCodeLabel")
        self.UserIDTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.UserIDTextbox.setGeometry(QtCore.QRect(140, 40, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UserIDTextbox.setFont(font)
        self.UserIDTextbox.setObjectName("UserIDTextbox")
        self.AllBookDetailsText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.AllBookDetailsText.setGeometry(QtCore.QRect(60, 140, 541, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AllBookDetailsText.setFont(font)
        self.AllBookDetailsText.setObjectName("AllBookDetailsText")
        self.BorrowBookButton = QtWidgets.QPushButton(self.centralwidget)
        self.BorrowBookButton.setGeometry(QtCore.QRect(370, 300, 221, 61))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BorrowBookButton.setFont(font)
        self.BorrowBookButton.setStyleSheet("background-color: 00000000;\n"
"  color: white;\n"
"  border: 4px solid white;\n"
"  border-radius: 30%;")
        self.BorrowBookButton.setObjectName("BorrowBookButton")
        self.BorrowBookButton.clicked.connect(self.click)

        BorrowBook.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BorrowBook)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 26))
        self.menubar.setObjectName("menubar")
        BorrowBook.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BorrowBook)
        self.statusbar.setObjectName("statusbar")
        BorrowBook.setStatusBar(self.statusbar)

        self.retranslateUi(BorrowBook)
        QtCore.QMetaObject.connectSlotsByName(BorrowBook)
    def click(self):
        print ("It works")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setStatusTip(_translate("MainWindow", "No errors."))
        self.UserIDLabel.setText(_translate("MainWindow", "User ID:"))
        self.BookCodeLabel.setText(_translate("MainWindow", "Book Codes (Seperate each book code with commas):"))
        self.BorrowBookButton.setText(_translate("MainWindow", "Borrow Book"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
