# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RunScreen7Test.ui'
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
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
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
        self.InstructionLabel = QtWidgets.QLabel(self.Home)
        self.InstructionLabel.setGeometry(QtCore.QRect(60, 40, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.InstructionLabel.setFont(font)
        self.InstructionLabel.setObjectName("InstructionLabel")
        self.InstructionText = QtWidgets.QTextBrowser(self.Home)
        self.InstructionText.setGeometry(QtCore.QRect(50, 80, 571, 361))
        self.InstructionText.setObjectName("InstructionText")
        self.stackedWidget.addWidget(self.Home)
        self.Search = QtWidgets.QWidget()
        self.Search.setStyleSheet("background-color: #949996")
        self.Search.setObjectName("Search")
        self.LocLabel = QtWidgets.QLabel(self.Search)
        self.LocLabel.setGeometry(QtCore.QRect(70, 90, 61, 21))
        self.LocLabel.setObjectName("LocLabel")
        self.DistLabel = QtWidgets.QLabel(self.Search)
        self.DistLabel.setGeometry(QtCore.QRect(70, 170, 47, 13))
        self.DistLabel.setObjectName("DistLabel")
        self.PRLabel = QtWidgets.QLabel(self.Search)
        self.PRLabel.setGeometry(QtCore.QRect(70, 250, 71, 21))
        self.PRLabel.setObjectName("PRLabel")
        self.SubmitButton = QtWidgets.QPushButton(self.Search)
        self.SubmitButton.setGeometry(QtCore.QRect(230, 350, 171, 61))
        self.SubmitButton.setObjectName("SubmitButton")
        self.SearchHeader = QtWidgets.QLabel(self.Search)
        self.SearchHeader.setGeometry(QtCore.QRect(110, 10, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.SearchHeader.setFont(font)
        self.SearchHeader.setObjectName("SearchHeader")
        self.HeaderLine1 = QtWidgets.QFrame(self.Search)
        self.HeaderLine1.setGeometry(QtCore.QRect(0, 50, 651, 20))
        self.HeaderLine1.setFrameShape(QtWidgets.QFrame.HLine)
        self.HeaderLine1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.HeaderLine1.setObjectName("HeaderLine1")
        self.LocLineEdit = QtWidgets.QLineEdit(self.Search)
        self.LocLineEdit.setGeometry(QtCore.QRect(152, 90, 351, 31))
        self.LocLineEdit.setText("")
        self.LocLineEdit.setObjectName("LocLineEdit")
        self.DistLineEdit = QtWidgets.QLineEdit(self.Search)
        self.DistLineEdit.setGeometry(QtCore.QRect(150, 170, 351, 31))
        self.DistLineEdit.setObjectName("DistLineEdit")
        self.PRComboBox = QtWidgets.QComboBox(self.Search)
        self.PRComboBox.setGeometry(QtCore.QRect(150, 250, 351, 31))
        self.PRComboBox.setObjectName("PRComboBox")
        self.PRComboBox.addItem("")
        self.PRComboBox.addItem("")
        self.PRComboBox.addItem("")
        self.PRComboBox.addItem("")
        self.stackedWidget.addWidget(self.Search)
        self.Sort = QtWidgets.QWidget()
        self.Sort.setStyleSheet("background-color: #949996")
        self.Sort.setObjectName("Sort")
        self.HeaderLine2 = QtWidgets.QFrame(self.Sort)
        self.HeaderLine2.setGeometry(QtCore.QRect(0, 50, 651, 20))
        self.HeaderLine2.setFrameShape(QtWidgets.QFrame.HLine)
        self.HeaderLine2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.HeaderLine2.setObjectName("HeaderLine2")
        self.SortHeader = QtWidgets.QLabel(self.Sort)
        self.SortHeader.setGeometry(QtCore.QRect(110, 10, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.SortHeader.setFont(font)
        self.SortHeader.setObjectName("SortHeader")
        self.SortText = QtWidgets.QTextBrowser(self.Sort)
        self.SortText.setGeometry(QtCore.QRect(25, 81, 601, 421))
        self.SortText.setObjectName("SortText")
        self.stackedWidget.addWidget(self.Sort)
        self.Roulette = QtWidgets.QWidget()
        self.Roulette.setStyleSheet("background-color: #949996")
        self.Roulette.setObjectName("Roulette")
        self.HeaderLine3 = QtWidgets.QFrame(self.Roulette)
        self.HeaderLine3.setGeometry(QtCore.QRect(0, 50, 651, 20))
        self.HeaderLine3.setFrameShape(QtWidgets.QFrame.HLine)
        self.HeaderLine3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.HeaderLine3.setObjectName("HeaderLine3")
        self.RouletteHeader = QtWidgets.QLabel(self.Roulette)
        self.RouletteHeader.setGeometry(QtCore.QRect(110, 10, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.RouletteHeader.setFont(font)
        self.RouletteHeader.setObjectName("RouletteHeader")
        self.stackedWidget.addWidget(self.Roulette)
        self.RouletteButton = QtWidgets.QPushButton(self.centralwidget)
        self.RouletteButton.setGeometry(QtCore.QRect(10, 300, 111, 41))
        self.RouletteButton.setObjectName("RouletteButton")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(10, 140, 111, 41))
        self.SearchButton.setObjectName("SearchButton")
        self.SortButton = QtWidgets.QPushButton(self.centralwidget)
        self.SortButton.setGeometry(QtCore.QRect(10, 220, 111, 41))
        self.SortButton.setObjectName("SortButton")
        self.MainLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainLabel.setGeometry(QtCore.QRect(130, 10, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.MainLabel.setFont(font)
        self.MainLabel.setObjectName("MainLabel")
        self.InstructionButton = QtWidgets.QPushButton(self.centralwidget)
        self.InstructionButton.setGeometry(QtCore.QRect(20, 70, 91, 31))
        self.InstructionButton.setObjectName("InstructionButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Restuarant Deciding App (V1.1)"))
        self.InstructionLabel.setText(_translate("MainWindow", "Instructions"))
        self.InstructionText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">This is a step by step guide to use the Restauarant Deciding App Version1.1.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">On this side of the screen you will see different tabs which corresponds to each stage of the decision process.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1- Search:  Here you will input  location (postcode or city), Distance (in miles) and Price Range of restaurants you want to find in your area. Once you\'ve filled in these parameters you submit and move onto step 2.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2- Sort: Here a you will go through up to 20 restaurants that met your criterion set up in step 1. You can press the Like button if you want to eat there; or the Dislike button if you wouldn\'t eat there. Once done press finished</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3- Roulette: This is the final stage where it will randomly select a restaurant based on your likes. </span></p></body></html>"))
        self.LocLabel.setText(_translate("MainWindow", "Location:"))
        self.DistLabel.setText(_translate("MainWindow", "Distance"))
        self.PRLabel.setText(_translate("MainWindow", "Price Range"))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))
        self.SearchHeader.setText(_translate("MainWindow", "Please fill out the form to get started!"))
        self.LocLineEdit.setPlaceholderText(_translate("MainWindow", "E.g. London or SE14 6NW"))
        self.DistLineEdit.setPlaceholderText(_translate("MainWindow", "E.g. 5 (miles)"))
        self.PRComboBox.setItemText(0, _translate("MainWindow", "£"))
        self.PRComboBox.setItemText(1, _translate("MainWindow", "££"))
        self.PRComboBox.setItemText(2, _translate("MainWindow", "£££"))
        self.PRComboBox.setItemText(3, _translate("MainWindow", "££££"))
        self.SortHeader.setText(_translate("MainWindow", "Like or Dislike a restaurant"))
        self.SortText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No restaurants as of now...</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.RouletteHeader.setText(_translate("MainWindow", "Spin the Roulette to get a restaurant!"))
        self.RouletteButton.setText(_translate("MainWindow", "3) Roulette"))
        self.SearchButton.setText(_translate("MainWindow", "1) Search"))
        self.SortButton.setText(_translate("MainWindow", "2) Sort"))
        self.MainLabel.setText(_translate("MainWindow", "Welcome to Restaurant Deciding App V1.1!"))
        self.InstructionButton.setText(_translate("MainWindow", "How to Use"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
