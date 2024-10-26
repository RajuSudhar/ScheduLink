import database
import bcrypt
from .logging import log_error

def register_user(username: str, fullname: str, email: str, password: str, phone: str | None):
    password_hash = hash_password(password)
    params = (username, fullname, email, password_hash, phone)
    database.insert_user(params)

def login_user(identifier: str, password: str):
    try:
        user = database.get_user_by_identifier(identifier)
        if not user:
            return {"status": "fail", "message": "User not found."}

        stored_hashed_password = user['password']

        if bcrypt.checkpw(password.encode(), stored_hashed_password.encode()):
            return {
                "status": "success",
                "message": "Login successful.",
                "user_data": {
                    "user_id": user['id'],
                    "username": user['username'],
                    "email": user['email'],
                }
            }
        else:
            return {"status": "fail", "message": "Invalid password."}

    except Exception as e:
        log_error(f"Error during login: {e}")
        return {"status": "error", "message": "An error occurred during login. Please try again."}

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

def generate_jwt_token():
    pass

def decode_jwt_token():
    pass

def get_current_user():
    pass

def reset_password_request():
    pass

def reset_password():
    pass

def logout_user():
    pass

def refresh_token():
    pass

