# login_init.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt, QPoint, Signal
from login_uit import Ui_MainWindow
from db_manager_t import DatabaseManager
from home_initt import MainWindow 

class LoginWindow(QMainWindow):
    login_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(100, 100, 1000, 580)
        self.setFixedSize(1000, 580)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.usernameLineEdit, self.passwordLineEdit, self.fullnameLineEdit = self.ui.usernameLineEdit, self.ui.passwordLineEdit, self.ui.fullnameLineEdit
        self.ui.close_button.clicked.connect(self.close)
        self.ui.minimize_button.clicked.connect(self.showMinimized)
        self.draggable = False
        self.offset = QPoint()
        self.db_manager = DatabaseManager()
        self.ui.register_pushButton.clicked.connect(self.register_user)
        self.ui.login_pushButton.clicked.connect(self.login_user)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.draggable:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False

    def register_user(self):
        fullname = self.fullnameLineEdit.text().strip()
        username = self.ui.usernameLineEdit_2.text().strip()
        email = self.ui.mailLineEdit.text().strip()
        phone = self.ui.phoneLineEdit.text().strip()
        password = self.ui.passwordLineEdit_2.text().strip()

        if fullname and username and email and phone and password:
            if self.db_manager.register_user(fullname, username, email, phone, password):
                QMessageBox.information(self, "Registration Successful", "You have been registered successfully!")
            else:
                QMessageBox.critical(self, "Registration Failed", "Failed to register. Please try again later.")
        else:
            QMessageBox.warning(self, "Incomplete Information", "Please fill in all fields.")

    def login_user(self):
        username = self.usernameLineEdit.text().strip()
        password = self.passwordLineEdit.text().strip()

        if username and password:
            user = self.db_manager.login_user(username, password)
            if user:
                QMessageBox.information(self, "Login Successful", "Welcome back, " + user[1] + "!")
                user_id = user[0]  # Retrieve user ID from the database
                self.login_signal.emit(str(user_id))
                self.close()  # Close the login window
                home_window = MainWindow(user_id)  # Pass user_id to the HomeWindow constructor
                home_window.show()

                QMessageBox.critical(self, "Login Failed", "Invalid username or password. Please try again.")
        else:
            QMessageBox.warning(self, "Incomplete Information", "Please fill in both username and password.")

def main():
    """Main function to start the application."""
    app = QApplication(sys.argv)
    
    # Create instances of both login and home windows
    login_window = LoginWindow()
    home_window = MainWindow()  # Assuming this is your home window
    
    # Connect the login signal to the receive_user_id slot in home_window
    login_window.login_signal.connect(home_window.receive_user_id)
    
    # Show the login window
    login_window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
