# # createAccountView.py

# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

# from frontend.ViewsController import ViewsController  # Importe a classe do controlador principal

# class Ui_CreateAccount(object):

#     def setupUi(self, MainWindow, controller):
#         if not MainWindow.objectName():
#             MainWindow.setObjectName(u"MainWindow")
#         MainWindow.resize(800, 600)
#         QMetaObject.connectSlotsByName(MainWindow)
#         self.centralwidget = QWidget(MainWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
#         self.pushButton = QPushButton(self.centralwidget)
#         self.pushButton.setObjectName(u"pushButton")
#         self.pushButton.setGeometry(QRect(310, 190, 75, 23))
#         self.pushButton_2 = QPushButton(self.centralwidget)
#         self.pushButton_2.setObjectName(u"pushButton_2")
#         self.pushButton_2.setGeometry(QRect(320, 340, 75, 23))
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QMenuBar(MainWindow)
#         self.menubar.setObjectName(u"menubar")
#         self.menubar.setGeometry(QRect(0, 0, 800, 21))
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QStatusBar(MainWindow)
#         self.statusbar.setObjectName(u"statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#         self.retranslateUi(MainWindow)

#         self.controller = ViewsController() 

#         QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#         self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
#         self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Texto do botão", None))

#     def ooi(self):
#         print("funcionando!")

#     def closeLoginWindow(self):
#         self.login_window.close()
