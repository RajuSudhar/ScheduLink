# home_init.py
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QLineEdit, QWidget, QDialog, QVBoxLayout
from PySide6.QtGui import QIcon
from home_uit import Ui_Schedulink
from PySide6.QtCore import Slot, QRect
import pymysql

class MainWindow(QMainWindow):
    def __init__(self, user_id=None):
        super().__init__()
        self.ui = Ui_Schedulink()
        self.ui.setupUi(self)
        self.connection = None
        self.user_id = user_id
        self.check_database_connection()
        self.populate_upcoming_tab()
        self.apply_font_family(self, "LEMON MILK")
        central_layout = QVBoxLayout()
        central_layout.addWidget(self.ui.centralWigdet)
        central_widget = QWidget()
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)
        self.ui.new_meet.clicked.connect(self.add_new_meetup)

    def apply_font_family(self, widget, font_family):
        widget_font = widget.font()
        widget_font.setFamily(font_family)
        widget.setFont(widget_font)

        for child_widget in widget.findChildren(QWidget):
            self.apply_font_family(child_widget, font_family)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.centralWidget().resize(event.size())

    def check_database_connection(self):
        if not self.connection:
            try:
                self.connection = pymysql.connect(
                    host='localhost',
                    user='python',
                    password='Impython312',
                    database='schedulink_db'
                )
            except pymysql.Error as e:
                print(f"Error connecting to the database: {e}")

    def populate_upcoming_tab(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT title, start_date_time, location FROM meetups WHERE start_date_time > NOW()")
                meetups = cursor.fetchall()
                layout = QVBoxLayout()
                self.ui.Upcoming_Tab.setLayout(layout)

                for meetup in meetups:
                    title, start_date_time, location = meetup
                    meetup_label = QLabel(f"Title: {title}, Date: {start_date_time}, Location: {location}")
                    layout.addWidget(meetup_label)
        except pymysql.Error as e:
            print(f"Error: {e}")
        finally:
            if self.connection:
                self.connection.close()
    def add_new_meetup(self):
        # Create a dialog to input meetup details
        dialog = QDialog(self)
        dialog.setWindowTitle("Add New Meetup")

        # Create input fields for meetup title, description, and location
        title_label = QLabel("Title:")
        self.title_edit = QLineEdit()
        description_label = QLabel("Description:")
        self.description_edit = QLineEdit()
        location_label = QLabel("Location:")
        self.location_edit = QLineEdit()

        # Create a button to confirm the meetup creation
        confirm_button = QPushButton("Create Meetup")
        confirm_button.clicked.connect(self.add_new_meetup)

        # Create the new meetup button
        self.new_meet = QPushButton(self.centralWidget())
        self.new_meet.setObjectName(u"new_meet")
        self.new_meet.setGeometry(QRect(10, 10, 90, 40))
        self.new_meet.setStyleSheet("QPushButton#new_meet { border-radius: 20px; background-color: #007bff; color: #ffffff; }"
                                     "QPushButton#new_meet:hover { background-color: #0056b3; }")
        self.new_meet.clicked.connect(self.show_new_meetup_dialog)


        # Create layout for the dialog
        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(self.title_edit)
        layout.addWidget(description_label)
        layout.addWidget(self.description_edit)
        layout.addWidget(location_label)
        layout.addWidget(self.location_edit)
        layout.addWidget(confirm_button)

        dialog.setLayout(layout)

        # Show the dialog
        dialog.exec()

    def show_new_meetup_dialog(self):
        dialog = NewMeetupDialog(parent=self)
        dialog.exec_()
    
    @Slot(str)
    def receive_user_id(self, user_id):
        # Create an instance of MainWindow with the received user ID
        self.window = MainWindow(user_id)
        self.window.show()

class NewMeetupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create New Meetup")
        layout = QVBoxLayout()

        self.title_edit = QLineEdit()
        self.title_edit.setPlaceholderText("Title")
        layout.addWidget(self.title_edit)

        self.description_edit = QLineEdit()
        self.description_edit.setPlaceholderText("Description")
        layout.addWidget(self.description_edit)

        self.location_edit = QLineEdit()
        self.location_edit.setPlaceholderText("Location")
        layout.addWidget(self.location_edit)

        self.start_datetime_edit = QDateTimeEdit()
        self.start_datetime_edit.setDateTime(QDateTime.currentDateTime())
        self.start_datetime_edit.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.start_datetime_edit.setMinimumDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.start_datetime_edit)

        self.end_datetime_edit = QDateTimeEdit()
        self.end_datetime_edit.setDateTime(QDateTime.currentDateTime())
        self.end_datetime_edit.setDisplayFormat("yyyy-MM-dd HH:mm")
        self.end_datetime_edit.setMinimumDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.end_datetime_edit)

        create_button = QPushButton("Create")
        create_button.clicked.connect(self.create_new_meetup)
        layout.addWidget(create_button)

        self.setLayout(layout)
    def create_new_meetup(self):
        title = self.title_edit.text().strip()
        description = self.description_edit.text().strip()
        location = self.location_edit.text().strip()
        start_datetime = self.start_datetime_edit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        end_datetime = self.end_datetime_edit.dateTime().toString("yyyy-MM-dd HH:mm:ss")

        if title and location:
            # Call the create_new_meetup function from DatabaseManager
            if self.parent().db_manager.create_new_meetup(title, description, start_datetime, end_datetime, location, self.parent().user_id):
                QMessageBox.information(self, "Success", "Meetup created successfully!")
                self.accept()
            else:
                QMessageBox.critical(self, "Error", "Failed to create meetup.")
        else:
            QMessageBox.warning(self, "Incomplete Information", "Please fill in title and location.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    user_id = "12345"  # Placeholder for actual user ID
    window = MainWindow(user_id)
    window.show()
    sys.exit(app.exec())
