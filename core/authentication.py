import sqlite3
import bcrypt
from datetime import datetime

DATABASE_PATH = "database/database.db"


# =====================================
# PASSWORD FUNCTIONS
# =====================================


def hash_password(password):
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode(), salt)
    return password_hash.decode()


def verify_password(password, stored_hash):
    return bcrypt.checkpw(password.encode(), stored_hash.encode())


# =====================================
# LOGGING FUNCTIONS
# =====================================


def add_log(user_id, action, status):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
    INSERT INTO logs (
        user_id,
        action,
        status
    )
    VALUES (?, ?, ?)
    """,
        (user_id, action, status),
    )

    conn.commit()
    conn.close()


def add_security_event(user_id, event_type, description):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
    INSERT INTO security_events (
        user_id,
        event_type,
        description
    )
    VALUES (?, ?, ?)
    """,
        (user_id, event_type, description),
    )

    conn.commit()
    conn.close()


# =====================================
# CHECK EXISTING USER
# =====================================


def email_exists(email):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE email = ?", (email,))

    result = cursor.fetchone()

    conn.close()

    return result is not None


# =====================================
# UPDATE PASSWORD
# =====================================


def update_password(email, new_password):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    password_hash = hash_password(new_password)

    cursor.execute(
        """
        UPDATE users
        SET password_hash = ?
        WHERE email = ?
        """,
        (password_hash, email),
    )

    conn.commit()

    success = cursor.rowcount > 0

    conn.close()

    return success


def username_exists(username):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))

    result = cursor.fetchone()

    conn.close()

    return result is not None


# =====================================
# REGISTER USER
# =====================================


def register_user(username, email, password, role="user"):

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    try:

        password_hash = hash_password(password)

        cursor.execute(
            """
        INSERT INTO users (
            username,
            email,
            password_hash,
            role
        )
        VALUES (?, ?, ?, ?)
        """,
            (username, email, password_hash, role),
        )

        conn.commit()

        user_id = cursor.lastrowid

        add_log(user_id, "REGISTER", "SUCCESS")

        print(f"User '{username}' registered successfully!")

        return {"success": True, "message": "User Registered Successfully"}

    except sqlite3.IntegrityError:

        add_security_event(
            None,
            "DUPLICATE_USERNAME",
            f"Registration attempted with existing username/email: {username}",
        )

        print("Username or Email already exists!")

        return {"success": False, "message": "Username or Email Already Exists"}

    finally:

        conn.close()


# =====================================
# LOGIN USER
# =====================================


def login_user(username, password):

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
    SELECT id,
           password_hash,
           role,
           account_status
    FROM users
    WHERE username = ?
    """,
        (username,),
    )

    user = cursor.fetchone()

    if not user:

        add_security_event(
            None, "USER_NOT_FOUND", f"Unknown username login attempt: {username}"
        )

        conn.close()

        return {"success": False, "message": "User Not Found"}

    user_id = user[0]
    stored_hash = user[1]
    role = user[2]
    account_status = user[3]

    if account_status != "active":

        add_security_event(
            user_id, "ACCOUNT_DISABLED", f"Disabled account login attempt: {username}"
        )

        conn.close()

        return {"success": False, "message": "Account Disabled"}

    if verify_password(password, stored_hash):

        cursor.execute(
            """
        UPDATE users
        SET last_login = ?
        WHERE id = ?
        """,
            (datetime.now(), user_id),
        )

        conn.commit()

        add_log(user_id, "LOGIN", "SUCCESS")

        conn.close()

        return {"success": True, "user_id": user_id, "username": username, "role": role}

    add_log(user_id, "LOGIN", "FAILED")

    add_security_event(
        user_id, "INVALID_PASSWORD", f"Wrong password entered for user: {username}"
    )

    conn.close()

    return {"success": False, "message": "Invalid Password"}


# =====================================
# TESTING
# =====================================

if __name__ == "__main__":

    result = login_user("admin", "admin123")

    print(result)
