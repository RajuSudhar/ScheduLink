import os
from dotenv import load_dotenv
from mysql.connector import connect, Error
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

def connect_db() -> PooledMySQLConnection | MySQLConnectionAbstract:
    connection = connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return connection

def disconnect_db(connection : PooledMySQLConnection | MySQLConnectionAbstract) -> None:
    connection.close()
    return None

def execute_query(query: str, params=None, fetch_one=False):
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query, params)
        if "SELECT" in query:
            return cursor.fetchone() if fetch_one else cursor.fetchall()
        elif "INSERT" in query:
            connection.commit()
            return cursor.lastrowid
        else:
            connection.commit()
            return None
    except Error as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()
        connection.close()

def get_user_by_identifier(identifier: str):
    query = "SELECT * FROM Users WHERE username = %s OR email = %s"
    return execute_query(query,(identifier,identifier), True)

def insert_user(params):
    query = """
    INSERT INTO Users (username, full_name, email, password_hash, phone)
    VALUES (%s, %s, %s, %s, %s)
    """
    return execute_query(query, params)

def get_meetup_by_id():
    pass

def insert_meetup():
    pass

def add_participants_to_meetup():
    pass

def remove_participant_from_meetup():
    pass

def get_meetup_participants():
    pass

def delete_meetup():
    pass


"""
def fetch_one(query: str, param = None):
    connection = connect_db()
    result = None
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, param)
            result = cursor.fetchone()
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            disconnect_db(connection)
    return result

def fetch_all(query: str, param = None):
    connection = connect_db()
    result = []
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, param)
            result = cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            disconnect_db(connection)
    return result
"""
