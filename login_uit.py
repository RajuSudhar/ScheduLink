import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QMainWindow, QWidget, QFrame, QLabel, QStatusBar
from PySide6.QtCore import Qt, QEvent, QObject, QCoreApplication, QRect, QSize, QMetaObject
from PySide6.QtGui import QFont

class EventFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn and isinstance(obj, QLineEdit):
            obj.clear()
        elif event.type() == QEvent.FocusOut and isinstance(obj, QLineEdit) and obj.text() == "":
            obj.setText(obj.placeholderText())
        return super().eventFilter(obj, event)

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 580)
        MainWindow.setStyleSheet(u"")
        self.event_filter = EventFilter()
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Titlebar = QWidget(self.centralwidget)
        self.Titlebar.setObjectName(u"Titlebar")
        self.Titlebar.setGeometry(QRect(0, 0, 1000, 30))
        self.Titlebar.setStyleSheet(
            "QWidget#Titlebar {"
            "   background-color: rgb(255, 255, 255);"
            "   border-top-left-radius: 10px;"
            "   border-top-right-radius: 10px;"
            "}"
        )

        font = QFont()
        font.setFamilies(["LEMON MILK"])
        font.setPointSize(8)
        font.setBold(True)

        self.close_button = QPushButton(self.Titlebar)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(975, 0, 25, 25))
        self.close_button.setFont(font)
        self.close_button.setStyleSheet(
            "QPushButton {"
            "   background-color: transparent;"
            "   border: none;"
            "   icon: url(close_icon.png);"
            "   width: 25px;"
            "   height: 25px;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgba(255, 0, 0, 0.2);"
            "}"
            "QPushButton:pressed {"
            "   background-color: rgba(255, 0, 0, 0.4);"
            "}"
        )

        self.minimize_button = QPushButton(self.Titlebar)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(950, 0, 25, 25))
        self.minimize_button.setFont(font)
        self.minimize_button.setStyleSheet(
            "QPushButton {"
            "   background-color: transparent;"
            "   border: none;"
            "   icon: url(minimize_icon.png);"
            "   width: 25px;"
            "   height: 25px;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgba(0, 0, 255, 0.2);"
            "}"
            "QPushButton:pressed {"
            "   background-color: rgba(0, 0, 255, 0.4);"
            "}"
        )
        self.LR = QFrame(self.centralwidget)
        self.LR.setObjectName(u"LR")
        self.LR.setGeometry(QRect(0, 90, 1000, 470))
        self.LR.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 170, 255), stop:1 rgb(0, 28, 85));")
        self.LR.setFrameShape(QFrame.StyledPanel)
        self.LR.setFrameShadow(QFrame.Raised)
        self.Login = QWidget(self.LR)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(70, 70, 320, 320))
        
        self.label_1 = QLabel(self.Login)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(90, 30, 120, 50))
        font2 = QFont()
        font2.setFamilies([u"LEMON MILK"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.label_1.setFont(font2)
        self.label_1.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.label_1.setAlignment(Qt.AlignCenter)
        self.usernameLineEdit = QLineEdit(self.Login)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(30, 120, 250, 30))
        self.usernameLineEdit.setStyleSheet(
            """
            QLineEdit {
                color: rgb(150, 150, 150);
                border: 0.5px solid rgb(150, 150, 150);
                border-radius: 5px;
            }
            """
        )
        self.passwordLineEdit = QLineEdit(self.Login)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(30, 170, 250, 30))
        self.passwordLineEdit.setStyleSheet(
            """
            QLineEdit {
                color: rgb(150, 150, 150);
                border: 0.5px solid rgb(150, 150, 150);
                border-radius: 5px;
            }
            """
        )
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.login_pushButton = QPushButton(self.Login)
        self.login_pushButton.setObjectName(u"login_pushButton")
        self.login_pushButton.setGeometry(QRect(110, 230, 100, 30))
        self.login_pushButton.setFont(font)
        self.login_pushButton.setAutoFillBackground(False)
        self.login_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.Register = QWidget(self.LR)
        self.Register.setObjectName(u"Register")
        self.Register.setGeometry(QRect(550, 20, 380, 420))
        self.label_2 = QLabel(self.Register)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 0, 150, 50))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(0, 170, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.fullnameLineEdit = QLineEdit(self.Register)
        self.fullnameLineEdit.setObjectName(u"fullnameLineEdit")
        self.fullnameLineEdit.setGeometry(QRect(60, 100, 250, 30))
        self.fullnameLineEdit.setStyleSheet(
            """
            QLineEdit {
                color: rgb(150, 150, 150);
                border: 0.5px solid rgb(150, 150, 150);
                border-radius: 5px;
            }
            """
        )
        self.usernameLineEdit_2 = QLineEdit(self.Register)
        self.usernameLineEdit_2.setObjectName(u"usernameLineEdit_2")
        self.usernameLineEdit_2.setGeometry(QRect(60, 140, 250, 30))
        self.usernameLineEdit_2.setStyleSheet(
            """
            QLineEdit {
                color: rgb(150, 150, 150);
                border: 0.5px solid rgb(150, 150, 150);
                border-radius: 5px;
            }
            """
        )
        self.mailLineEdit = QLineEdit(self.Register)
        self.mailLineEdit.setObjectName(u"mailLineEdit")
        self.mailLineEdit.setGeometry(QRect(60, 180, 250, 30))
        self.mailLineEdit.setStyleSheet(
            """
            QLineEdit {
                color: rgb(150, 150, 150);
                border: 0.5px solid rgb(150, 150, 150);
                border-radius: 5px;
            }
            """
        )
        self.phoneLineEdit = QLineEdit(self.Register)
        self.phoneLineEdit.setObjectName(u"phoneLineEdit")
        self.phoneLineEdit.setGeometry(QRect(60, 220, 250, 30))
        self.phoneLineEdit.setStyleSheet("""
            QLineEdit {
                color: rgb(150, 150, 150);
                border: 0.5px solid rgb(150, 150, 150);
                border-radius: 5px;
            }
            """
        )
        self.passwordLineEdit_2 = QLineEdit(self.Register)
        self.passwordLineEdit_2.setObjectName(u"passwordLineEdit_2")
        self.passwordLineEdit_2.setGeometry(QRect(60, 260, 250, 30))
        self.passwordLineEdit_2.setStyleSheet("""
            QLineEdit {
                color: rgb(150, 150, 150);
                border: 0.5px solid rgb(150, 150, 150);
                border-radius: 5px;
            }
            """
        )
        self.passwordLineEdit_2.setEchoMode(QLineEdit.Password)
        self.repeatPasswordLineEdit = QLineEdit(self.Register)
        self.repeatPasswordLineEdit.setObjectName(u"repeatPasswordLineEdit")
        self.repeatPasswordLineEdit.setGeometry(QRect(60, 300, 250, 30))
        self.repeatPasswordLineEdit.setStyleSheet("""
            QLineEdit {
                color: rgb(150, 150, 150);
                border: 0.5px solid rgb(150, 150, 150);
                border-radius: 5px;
            }
            """
        )
        self.register_pushButton = QPushButton(self.Register)
        self.register_pushButton.setObjectName(u"register_pushButton")
        self.register_pushButton.setGeometry(QRect(140, 360, 100, 30))
        self.register_pushButton.setFont(font)
        self.register_pushButton.setAutoFillBackground(False)
        self.register_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.Welcome = QWidget(self.centralwidget)
        self.Welcome.setObjectName(u"Welcome")
        self.Welcome.setGeometry(QRect(0, 30, 1000, 60))
        font3 = QFont()
        font3.setFamilies([u"Modern"])
        font3.setPointSize(12)
        self.Welcome.setFont(font3)
        self.Welcome.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Welcome_2 = QLabel(self.Welcome)
        self.Welcome_2.setObjectName(u"Welcome_2")
        self.Welcome_2.setGeometry(QRect(250, 0, 500, 50))
        font4 = QFont()
        font4.setFamilies([u"LEMON MILK Bold"])
        font4.setPointSize(22)
        font4.setBold(True)
        self.Welcome_2.setFont(font4)
        self.Welcome_2.setStyleSheet(u"color: rgb(0, 113, 227);")
        self.Welcome_2.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.Titlebar.setStyleSheet(
            "QWidget#Titlebar {"
            "   background-color: rgb(255, 255, 255);"
            "   border-top-left-radius: 10px;"
            "   border-top-right-radius: 10px;"
            "}"
        )

        self.LR.setStyleSheet(
            "QFrame#LR {"
            "   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 170, 255), stop:1 rgb(0, 28, 85));"
            "   border-top-left-radius: 0px;"
            "   border-top-right-radius: 0px;"
            "   border-bottom-left-radius: 10px;"  
            "   border-bottom-right-radius: 10px;"  
            "}"
        )

        self.Login.setStyleSheet(
            "QWidget#Login {"
            "   background-color: rgb(255, 255, 255);"
            "   border-radius: 10px;"
            "}"
        )

        self.Register.setStyleSheet(
            "QWidget#Register {"
            "background-color: rgb(255, 255, 255);"
            "   border-radius: 10px;"
            "}"
        )

        self.Welcome.setStyleSheet(
            "QWidget#Welcome {"
            "   background-color: rgb(255, 255, 255);"
            "}"
        )
        self.login_pushButton.setStyleSheet(
            "QPushButton {"
            "   color: rgb(255, 255, 255);"
            "   background-color: rgb(0, 170, 255);"
            "   border-radius: 10px;"
            "   padding: 5px 10px;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgba(0, 170, 255, 0.8);"
            "}"
            "QPushButton:pressed {"
            "   background-color: rgba(0, 170, 255, 0.5);"
            "}"
        )

        self.register_pushButton.setStyleSheet(self.login_pushButton.styleSheet())


        return self.usernameLineEdit, self.passwordLineEdit, self.fullnameLineEdit
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.close_button.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.minimize_button.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login_pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.fullnameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.usernameLineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.mailLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mail ID", None))
        self.phoneLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.passwordLineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.repeatPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repeat Password", None))
        self.register_pushButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.Welcome_2.setText(QCoreApplication.translate("MainWindow", u"Welcome to Schedulink", None))
    # retranslateUi

