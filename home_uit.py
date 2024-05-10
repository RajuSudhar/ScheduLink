from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QWidget)

class Ui_Schedulink(object):
    def setupUi(self, Schedulink):
        if not Schedulink.objectName():
            Schedulink.setObjectName(u"Schedulink")
        Schedulink.setEnabled(True)
        Schedulink.resize(800, 600)
        self.centralwidget = QWidget(Schedulink)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralWigdet = QWidget(self.centralwidget)
        self.centralWigdet.setObjectName(u"centralWigdet")
        self.centralWigdet.setGeometry(QRect(0, 0, 800, 600))
        font = QFont()
        font.setFamilies([u"LEMON MILK"])
        font.setPointSize(9)
        font.setBold(True)
        self.centralWigdet.setFont(font)
        self.centralWigdet.setStyleSheet("background-color: #ffffff;")  # Set background color of the central widget

        self.new_meet = QPushButton(self.centralWigdet)
        self.new_meet.setObjectName(u"new_meet")
        self.new_meet.setGeometry(QRect(10, 10, 90, 40))
        self.new_meet.setStyleSheet("QPushButton#new_meet { border-radius: 20px; background-color: #007bff; color: #ffffff; }"
                                     "QPushButton#new_meet:hover { background-color: #0056b3; }")
        
        self.dashboard = QTabWidget(self.centralWigdet)
        self.dashboard.setObjectName(u"dashboard")
        self.dashboard.setGeometry(QRect(10, 70, 780, 510))
        self.dashboard.setStyleSheet("QTabWidget::pane { border-radius: 10px; background-color: #ffffff; }"
                                      "QTabWidget::tab-bar { alignment: center; }"
                                      "QTabBar::tab { border-radius: 10px; min-width: 100px; min-height: 40px; background-color: #ffffff; }"
                                      "QTabBar::tab:selected { background-color: #007bff; color: #ffffff; }"
                                      "QTabBar::tab:hover { background-color: #0056b3; }")
        self.dashboard.setTabBarAutoHide(False)
        self.Upcoming_Tab = QWidget()
        self.Upcoming_Tab.setObjectName(u"Upcoming_Tab")
        self.Upcoming_Tab.setFont(font)
        self.dashboard.addTab(self.Upcoming_Tab, "")
        self.All_Tab = QWidget()
        self.All_Tab.setObjectName(u"All_Tab")
        self.All_Tab.setFont(font)
        self.All_Tab.setStyleSheet("QWidget { border-radius: 10px; background-color: #ffffff; }")
        self.dashboard.addTab(self.All_Tab, "")
        
        self.profile = QPushButton(self.centralWigdet)
        self.profile.setObjectName(u"profile")
        self.profile.setGeometry(QRect(680, 20, 90, 40))
        self.profile.setStyleSheet("QPushButton#profile { border-radius: 20px; background-color: #007bff; color: #ffffff; }"
                                     "QPushButton#profile:hover { background-color: #0056b3; }")
        
        Schedulink.setCentralWidget(self.centralwidget)

        self.retranslateUi(Schedulink)

        self.dashboard.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(Schedulink)
    # setupUi

    def retranslateUi(self, Schedulink):
        Schedulink.setWindowTitle(QCoreApplication.translate("Schedulink", u"Schedulink", None))
        self.new_meet.setText(QCoreApplication.translate("Schedulink", u"+ New", None))
        self.dashboard.setTabText(self.dashboard.indexOf(self.Upcoming_Tab), QCoreApplication.translate("Schedulink", u"Upcoming", None))
        self.dashboard.setTabText(self.dashboard.indexOf(self.All_Tab), QCoreApplication.translate("Schedulink", u"All", None))
        self.profile.setText(QCoreApplication.translate("Schedulink", u"Profile", None))
    # retranslateUi
