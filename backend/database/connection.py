import sqlite3

connection = sqlite3.connect("weather_app_db.db")

connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
        
        user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_email TEXT NOT NULL,
        user_name TEXT NOT NULL,
        user_password TEXT NOT NULL,
        user_creation DATETIME NOT NULL
    )
""")




