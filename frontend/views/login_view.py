from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(692, 600)
        MainWindow.setWindowFlags(
            Qt.Window |
            Qt.WindowMinimizeButtonHint |
            Qt.WindowCloseButtonHint  # Add this line to keep the close button
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 691, 571))
        self.frame.setCursor(QCursor(Qt.ArrowCursor))
        self.frame.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 40, 361, 181))
        self.label.setPixmap(QPixmap(u"../weather-app/frontend/assets/cloudy_sun_mainscreen.png"))
        self.label.setScaledContents(True)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(140, 240, 371, 301))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.txt_name = QLineEdit(self.frame_2)
        self.txt_name.setObjectName(u"txt_name")
        self.txt_name.setGeometry(QRect(50, 60, 251, 20))
        self.txt_name.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(85, 255, 255);")
        self.txt_name.setEchoMode(QLineEdit.Normal)
        self.txt_name.setCursorPosition(0)
        self.txt_name.setAlignment(Qt.AlignCenter)
        self.txt_name.setDragEnabled(False)
        self.txt_password = QLineEdit(self.frame_2)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(50, 130, 251, 20))
        self.txt_password.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_password.setAlignment(Qt.AlignCenter)
        self.btn_entrar = QPushButton(self.frame_2)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(130, 170, 75, 23))
        self.btn_entrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrar.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0,0,0);\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,0,0)\n"
"\n"
"}\n"
"\n"
"\n"
"	")
        self.btn_entrar.clicked.connect(self.btn_print)
        self.btn_criar_conta = QPushButton(self.frame_2)
        self.btn_criar_conta.setObjectName(u"btn_criar_conta")
        self.btn_criar_conta.setGeometry(QRect(130, 220, 75, 23))
        self.btn_criar_conta.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_criar_conta.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0,0,0);\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255,255,255);\n"
"	color: rgb(0,0,0)\n"
"\n"
"}\n"
"\n"
"\n"
"	")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 692, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("LOGIN", u"LOGIN", None))
        self.label.setText("")
        self.txt_name.setInputMask("")
        self.txt_name.setText("")
        self.txt_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txt_password.setText("")
        self.txt_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.btn_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.btn_criar_conta.setText(QCoreApplication.translate("MainWindow", u"Criar conta", None))


    def btn_print(self):
        print("Hello World!")




        