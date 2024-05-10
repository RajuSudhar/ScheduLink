import mysql.connector
from hashlib import sha256

class DatabaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="python",
            password="Impython312",
            database="schedulink_db"
        )
        self.cursor = self.connection.cursor()

    def register_user(self, fullname, username, email, phone, password):
        hashed_password = self.hash_password(password)
        query = "INSERT INTO Users (full_name, username, email_address, phone, password_hash) VALUES (%s, %s, %s, %s, %s)"
        values = (fullname, username, email, phone, hashed_password)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print("Error:", err)
            return False

    def login_user(self, username, password):
        hashed_password = self.hash_password(password)
        query = "SELECT * FROM Users WHERE username = %s AND password_hash = %s"
        values = (username, hashed_password)
        self.cursor.execute(query, values)
        user = self.cursor.fetchone()
        return user

    def hash_password(self, password):
        return sha256(password.encode()).hexdigest()

    def retrieve_upcoming_meetups(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Meetups WHERE start_datetime > NOW()")
            upcoming_meetups = cursor.fetchall()
            cursor.close()
            return upcoming_meetups
        except mysql.connector.Error as err:
            print("Error retrieving upcoming meetups:", err)
            return []

    def create_new_meetup(self, title, description, start_datetime, end_datetime, location, organizer_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO Meetups (title, description, start_datetime, end_datetime, location, organizer_id) VALUES (%s, %s, %s, %s, %s, %s)",
                           (title, description, start_datetime, end_datetime, location, organizer_id))
            self.conn.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error creating new meetup:", err)
            return False

    def retrieve_meetup_participants(self, meetup_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM MeetupParticipants WHERE meetup_id = %s", (meetup_id,))
            participants = cursor.fetchall()
            cursor.close()
            return participants
        except mysql.connector.Error as err:
            print("Error retrieving meetup participants:", err)
            return []

    def add_participant_to_meetup(self, meetup_id, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO MeetupParticipants (meetup_id, user_id) VALUES (%s, %s)", (meetup_id, user_id))
            self.conn.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error adding participant to meetup:", err)
            return False

    def remove_participant_from_meetup(self, meetup_id, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM MeetupParticipants WHERE meetup_id = %s AND user_id = %s", (meetup_id, user_id))
            self.conn.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error removing participant from meetup:", err)
            return False

