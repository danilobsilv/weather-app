# import sys

# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

# from backend.controllers.userController import UserController

# from frontend.ViewsController import ViewsController

# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow, controller: ViewsController):  # Receba o controlador como argumento
#         if not MainWindow.objectName():
#             MainWindow.setObjectName(u"MainWindow")
#         MainWindow.setFixedSize(692, 600)
#         MainWindow.setWindowFlags(
#             Qt.Window |
#             Qt.WindowMinimizeButtonHint |
#             Qt.WindowCloseButtonHint)
#         icon = QIcon("../weather-app/frontend/assets/cloudy_sun_mainscreen.png")
#         MainWindow.setWindowIcon(icon)

#         self.controller = controller

#         self.window_builder = None
#         self.centralwidget = QWidget(MainWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
#         self.frame = QFrame(self.centralwidget)
#         self.frame.setObjectName(u"frame")
#         self.frame.setGeometry(QRect(0, 0, 771, 571))
#         self.frame.setCursor(QCursor(Qt.ArrowCursor))
#         self.frame.setStyleSheet(u"")
#         self.frame.setFrameShape(QFrame.StyledPanel)
#         self.frame.setFrameShadow(QFrame.Raised)

#         self.label = QLabel(self.frame)
#         self.label.setObjectName(u"label")
#         self.label.setGeometry(QRect(-30, 0, 801, 631))
#         self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);")
#         self.label.setPixmap(QPixmap(u"../weather-app/frontend/assets/terra_edit.png"))
#         self.label.setScaledContents(True)

#         self.frame_2 = QFrame(self.frame)
#         self.frame_2.setObjectName(u"frame_2")
#         self.frame_2.setGeometry(QRect(0, 220, 701, 291))
#         self.frame_2.setFrameShape(QFrame.StyledPanel)
#         self.frame_2.setFrameShadow(QFrame.Raised)

#         self.lineEdit = QLineEdit(self.frame_2)
#         self.lineEdit.setObjectName(u"lineEdit")
#         self.lineEdit.setGeometry(QRect(240, 80, 211, 20))
#         self.lineEdit.setAlignment(Qt.AlignCenter)
#         self.lineEdit.setStyleSheet(u"background: transparent;\n"
#                                     u"border: none;\n"
#                                     u"border-bottom: 1px solid white;\n"
#                                     u"color: white;")

#         self.lineEdit_2 = QLineEdit(self.frame_2)
#         self.lineEdit_2.setObjectName(u"lineEdit_2")
#         self.lineEdit_2.setGeometry(QRect(240, 140, 211, 20))
#         self.lineEdit_2.setAlignment(Qt.AlignCenter)
#         self.lineEdit_2.setEchoMode(QLineEdit.Password)
#         self.lineEdit_2.setStyleSheet(u"background: transparent;\n"
#                                       u"border: none;\n"
#                                       u"border-bottom: 1px solid white;\n"
#                                       u"color: white;")

#         self.btn_entrar = QPushButton(self.frame_2)
#         self.btn_entrar.setObjectName(u"btn_entrar")
#         self.btn_entrar.setGeometry(QRect(300, 190, 75, 23))
#         self.btn_entrar.setCursor(QCursor(Qt.PointingHandCursor))
#         self.btn_entrar.clicked.connect(self.GoToMainScreen)
#         # self.btn_entrar.clicked.connect(self.getLineEdit)
#         self.btn_entrar.setStyleSheet(u"QPushButton {\n"
#                                       "    background-color: rgb(255, 255, 255);\n"
#                                       "    color: rgb(0, 0, 0);\n"
#                                       "    border-radius: 10px;\n"
#                                       "}\n"
#                                       "\n"
#                                       "QPushButton:hover {\n"
#                                       "    background-color: rgb(240, 240, 240);\n"
#                                       "    color: rgb(0, 0, 0);\n"
#                                       "}\n"
#                                       "")

#         self.btn_criarConta = QPushButton(self.frame_2)
#         self.btn_criarConta.setObjectName(u"btn_criarConta")
#         self.btn_criarConta.setGeometry(QRect(300, 240, 75, 23))
#         self.btn_criarConta.setCursor(QCursor(Qt.PointingHandCursor))
#         self.btn_criarConta.clicked.connect(self.goToCreateAccount)
#         self.btn_criarConta.setStyleSheet(u"QPushButton {\n"
#                                           "    background-color: rgb(255, 255, 255);\n"
#                                           "    color: rgb(0, 0, 0);\n"
#                                           "    border-radius: 10px;\n"
#                                           "}\n"
#                                           "\n"
#                                           "QPushButton:hover {\n"
#                                           "    background-color: rgb(240, 240, 240);\n"
#                                           "    color: rgb(0, 0, 0);\n"
#                                           "}\n"
#                                           "")

#         self.show_pass_button = QPushButton(self.frame_2)
#         self.show_pass_button.setObjectName(u"show_pass_button")
#         self.show_pass_button.setGeometry(QRect(460, 135, 25, 25))
#         self.show_pass_button.setCursor(QCursor(Qt.PointingHandCursor))
#         self.show_pass_button.setStyleSheet(u"QPushButton {\n"
#                                             "    background-color: transparent;\n"
#                                             "    border: none;\n"
#                                             "    icon-size: 20px;\n"
#                                             "}\n"
#                                             "\n"
#                                             "QPushButton:hover {\n"
#                                             "    icon-size: 22px;\n"
#                                             "}\n"
#                                             "")
#         self.show_pass_button.setIcon(QIcon("../weather-app/frontend/assets/eye_icon.ico"))
#         self.show_pass_button.setCheckable(True)
#         self.show_pass_button.setChecked(False)
#         self.show_pass_button.clicked.connect(self.toggleShowPassword)
#         self.show_pass_button.setIcon(QIcon("../weather-app/frontend/assets/eye_icon.ico"))
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QMenuBar(MainWindow)
#         self.menubar.setObjectName(u"menubar")
#         self.menubar.setGeometry(QRect(0, 0, 687, 21))
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QStatusBar(MainWindow)
#         self.statusbar.setObjectName(u"statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)
#         QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LOGIN", None))
#         self.label.setText("")
#         self.btn_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
#         self.btn_criarConta.setText(QCoreApplication.translate("MainWindow", u"Criar conta", None))
#         self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
#         self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))

#     def goToCreateAccount(self):
#         self.controller.showCreateAccountWindow()
            


#     def GoToMainScreen(self):
        
#         userC = UserController()
#         email_value = self.lineEdit.text()
#         password_value = self.lineEdit_2.text()

#         if userC.checkUserEmail(email_value) is True:
#             print("Tá TRUE")
#         else:
#             print("Tá FALSE")

#     def toggleShowPassword(self):
#         if self.show_pass_button.isChecked():
#             self.lineEdit_2.setEchoMode(QLineEdit.Normal)
#         else:
#             self.lineEdit_2.setEchoMode(QLineEdit.Password)


#     def sayHi(self):
#         print("hello world!")

#     def getLineEdit(self):
#         value = self.lineEdit.text()
#         print(value)
#         # print("cuzinho")
