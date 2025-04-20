"""Database programming"""

import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# Create table if not exists
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)"""
)
connection.commit()

# Insert data into the table (CORRECTED)
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
connection.commit()

# Read data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)  # Prints each row as a tuple

# Optional delete operation (commented)
# cursor.execute("DELETE FROM users WHERE name = ?", ('Bob',))
# connection.commit()

# Begin a transaction for update
try:
    cursor.execute("BEGIN")
    cursor.execute("UPDATE users SET age = ? WHERE name = ?", (32, "Bob"))
    connection.commit()
except Exception as e:
    print(f"An error occurred: {e}")
    connection.rollback()

# Close the connection
connection.close()
