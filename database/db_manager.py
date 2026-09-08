import sqlite3

DATABASE_PATH = "database/database.db"


# =====================================
# DATABASE CREATION
# =====================================


def create_database():

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # USERS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL,
        totp_secret TEXT,
        is_2fa_enabled INTEGER DEFAULT 0,
        account_status TEXT DEFAULT 'active',
        last_login TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # FILES TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        file_name TEXT NOT NULL,
        encrypted_path TEXT NOT NULL,
        original_size INTEGER,
        encrypted_size INTEGER,
        upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # LOGS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        action TEXT NOT NULL,
        status TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # SECURITY EVENTS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS security_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        event_type TEXT NOT NULL,
        description TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()

    print("Database created successfully!")


# =====================================
# VIEW USERS
# =====================================


def view_users():

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id,
           username,
           email,
           role,
           account_status,
           last_login,
           created_at
    FROM users
    ORDER BY id ASC
    """)

    users = cursor.fetchall()

    print("\n===== USERS =====")

    for user in users:
        print(user)

    conn.close()


# =====================================
# VIEW LOGS
# =====================================


def view_logs():

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT logs.id,
           users.username,
           users.email,
           logs.action,
           logs.status,
           logs.timestamp
    FROM logs
    LEFT JOIN users
    ON logs.user_id = users.id
    ORDER BY logs.timestamp DESC
    """)

    logs = cursor.fetchall()

    print("\n===== LOGS =====")

    for log in logs:
        print(log)

    conn.close()


# =====================================
# VIEW SECURITY EVENTS
# =====================================


def view_security_events():

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT security_events.id,
           users.username,
           users.email,
           security_events.event_type,
           security_events.description,
           security_events.timestamp
    FROM security_events
    LEFT JOIN users
    ON security_events.user_id = users.id
    ORDER BY security_events.timestamp DESC
    """)

    events = cursor.fetchall()

    print("\n===== SECURITY EVENTS =====")

    for event in events:
        print(event)

    conn.close()


# =====================================
# DATABASE STATS
# =====================================


def database_stats():

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Total Users
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    # Active Users
    cursor.execute("""
    SELECT COUNT(*)
    FROM users
    WHERE account_status = 'active'
    """)
    active_users = cursor.fetchone()[0]

    # Disabled Users
    cursor.execute("""
    SELECT COUNT(*)
    FROM users
    WHERE account_status != 'active'
    """)
    disabled_users = cursor.fetchone()[0]

    # Total Files
    cursor.execute("SELECT COUNT(*) FROM files")
    total_files = cursor.fetchone()[0]

    # Total Logs
    cursor.execute("SELECT COUNT(*) FROM logs")
    total_logs = cursor.fetchone()[0]

    # Total Security Events
    cursor.execute("SELECT COUNT(*) FROM security_events")
    total_events = cursor.fetchone()[0]

    conn.close()

    print("\n===== DATABASE STATS =====")
    print(f"Total Users      : {total_users}")
    print(f"Active Users     : {active_users}")
    print(f"Disabled Users   : {disabled_users}")
    print(f"Stored Files     : {total_files}")
    print(f"System Logs      : {total_logs}")
    print(f"Security Events  : {total_events}")


# =====================================
# TESTING
# =====================================

if __name__ == "__main__":

    create_database()

    print("\n==============================")
    print(" SECURE FILE VAULT DATABASE ")
    print("==============================")

    database_stats()

    # Uncomment when needed

    # view_users()
    # view_logs()
    # view_security_events()
