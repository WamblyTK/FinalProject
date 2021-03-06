# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RunScreen4Test.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(129, 69, 651, 521))
        self.stackedWidget.setStyleSheet("background-color:#949996")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Home.setObjectName("Home")
        self.label = QtWidgets.QLabel(self.Home)
        self.label.setGeometry(QtCore.QRect(60, 40, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.Home)
        self.textBrowser.setGeometry(QtCore.QRect(50, 80, 571, 361))
        self.textBrowser.setObjectName("textBrowser")
        self.stackedWidget.addWidget(self.Home)
        self.Red = QtWidgets.QWidget()
        self.Red.setStyleSheet("background-color: #949996")
        self.Red.setObjectName("Red")
        self.LocLabel = QtWidgets.QLabel(self.Red)
        self.LocLabel.setGeometry(QtCore.QRect(70, 90, 61, 21))
        self.LocLabel.setObjectName("LocLabel")
        self.DistLabel = QtWidgets.QLabel(self.Red)
        self.DistLabel.setGeometry(QtCore.QRect(70, 170, 47, 13))
        self.DistLabel.setObjectName("DistLabel")
        self.PRLabel = QtWidgets.QLabel(self.Red)
        self.PRLabel.setGeometry(QtCore.QRect(70, 250, 71, 21))
        self.PRLabel.setObjectName("PRLabel")
        self.SubLabel = QtWidgets.QPushButton(self.Red)
        self.SubLabel.setGeometry(QtCore.QRect(230, 350, 171, 61))
        self.SubLabel.setObjectName("SubLabel")
        self.SearchHeader = QtWidgets.QLabel(self.Red)
        self.SearchHeader.setGeometry(QtCore.QRect(110, 10, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.SearchHeader.setFont(font)
        self.SearchHeader.setObjectName("SearchHeader")
        self.HeaderSplit = QtWidgets.QFrame(self.Red)
        self.HeaderSplit.setGeometry(QtCore.QRect(0, 50, 651, 16))
        self.HeaderSplit.setFrameShape(QtWidgets.QFrame.HLine)
        self.HeaderSplit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.HeaderSplit.setObjectName("HeaderSplit")
        self.LocLineEdit = QtWidgets.QLineEdit(self.Red)
        self.LocLineEdit.setGeometry(QtCore.QRect(152, 90, 351, 31))
        self.LocLineEdit.setObjectName("LocLineEdit")
        self.DistLineEdit = QtWidgets.QLineEdit(self.Red)
        self.DistLineEdit.setGeometry(QtCore.QRect(150, 170, 351, 31))
        self.DistLineEdit.setObjectName("DistLineEdit")
        self.PRComboBox = QtWidgets.QComboBox(self.Red)
        self.PRComboBox.setGeometry(QtCore.QRect(150, 250, 351, 31))
        self.PRComboBox.setObjectName("PRComboBox")
        self.stackedWidget.addWidget(self.Red)
        self.Yellow = QtWidgets.QWidget()
        self.Yellow.setStyleSheet("background-color: #949996")
        self.Yellow.setObjectName("Yellow")
        self.stackedWidget.addWidget(self.Yellow)
        self.Blue = QtWidgets.QWidget()
        self.Blue.setStyleSheet("background-color: #949996")
        self.Blue.setObjectName("Blue")
        self.stackedWidget.addWidget(self.Blue)
        self.BButton = QtWidgets.QPushButton(self.centralwidget)
        self.BButton.setGeometry(QtCore.QRect(10, 300, 111, 41))
        self.BButton.setObjectName("BButton")
        self.RButton = QtWidgets.QPushButton(self.centralwidget)
        self.RButton.setGeometry(QtCore.QRect(10, 140, 111, 41))
        self.RButton.setObjectName("RButton")
        self.YButton = QtWidgets.QPushButton(self.centralwidget)
        self.YButton.setGeometry(QtCore.QRect(10, 220, 111, 41))
        self.YButton.setObjectName("YButton")
        self.MainLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainLabel.setGeometry(QtCore.QRect(130, 10, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.MainLabel.setFont(font)
        self.MainLabel.setObjectName("MainLabel")
        self.InstructionButton = QtWidgets.QPushButton(self.centralwidget)
        self.InstructionButton.setGeometry(QtCore.QRect(20, 70, 91, 31))
        self.InstructionButton.setObjectName("InstructionButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Restuarant Deciding App (V1.1)"))
        self.label.setText(_translate("MainWindow", "Instructions"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">This is a step by step guide to use the Restauarant Deciding App Version1.1.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">On this side of the screen you will see different tabs which corresponds to each stage of the decision process.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1- Search:  Here you will input  location (postcode or city), Distance (in miles) and Price Range of restaurants you want to find in your area. Once you\'ve filled in these parameters you submit and move onto step 2.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2- Sort: Here a you will go through up to 50 restaurants that met your criterion set up in step 1. You can press the Like button if you want to eat there; or the Dislike button if you wouldn\'t eat there. Once done press finished</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3- Roulette: This is the final stage where it will randomly select a restaurant based on your likes. </span></p></body></html>"))
        self.LocLabel.setText(_translate("MainWindow", "Location:"))
        self.DistLabel.setText(_translate("MainWindow", "Distance"))
        self.PRLabel.setText(_translate("MainWindow", "Price Range"))
        self.SubLabel.setText(_translate("MainWindow", "Submit"))
        self.SearchHeader.setText(_translate("MainWindow", "Please fill out the form to get started!"))
        self.BButton.setText(_translate("MainWindow", "3) Roulette"))
        self.RButton.setText(_translate("MainWindow", "1) Search"))
        self.YButton.setText(_translate("MainWindow", "2) Sort"))
        self.MainLabel.setText(_translate("MainWindow", "Welcome to Restuarant Deciding App V1.1!"))
        self.InstructionButton.setText(_translate("MainWindow", "How to Use"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
