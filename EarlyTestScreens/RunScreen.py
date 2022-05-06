
from PyQt5 import QtCore, QtGui, QtWidgets

#Main Window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #Set window size
        MainWindow.resize(800, 600)
        #Font
        font = QtGui.QFont()
        #Font Size
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Start Button
        self.Start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Button.setGeometry(QtCore.QRect(260, 200, 251, 61))
        self.Start_Button.setObjectName("Start_Button")
        #How to use button
        self.Instruction_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Instruction_Button.setGeometry(QtCore.QRect(260, 290, 251, 61))
        self.Instruction_Button.setObjectName("Instruction_Button")
        #Quit Button
        self.Quit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Quit_Button.setGeometry(QtCore.QRect(260, 380, 251, 61))
        self.Quit_Button.setObjectName("Quit_Button")
        #Title
        self.Title_label = QtWidgets.QLabel(self.centralwidget)
        self.Title_label.setGeometry(QtCore.QRect(250, 70, 271, 71))
        #Title Font
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Title_label.setFont(font)
        self.Title_label.setObjectName("Title_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #def Start_Pressed(self):    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Restuarant Deciding App (V1.1)"))
        self.Start_Button.setText(_translate("MainWindow", "Start"))
        self.Instruction_Button.setText(_translate("MainWindow", "How to use"))
        self.Quit_Button.setText(_translate("MainWindow", "Quit"))
        self.Title_label.setText(_translate("MainWindow", "Welcome to Restuarant Decider!"))
    
    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
