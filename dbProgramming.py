import mysql.connector

# Step 1: Connect to MySQL server (no database yet)
myconn = mysql.connector.connect(host="localhost", user="root", passwd="root")

mycur = myconn.cursor()

# Step 2: Create the database (only if it doesn't exist)
mycur.execute("CREATE DATABASE IF NOT EXISTS Collegedb")
print("Database created!")

# Close current connection and reconnect with database specified
mycur.close()
myconn.close()

# Step 3: Reconnect to the database you just created
myconn = mysql.connector.connect(
    host="localhost", user="root", passwd="root", database="Collegedb"
)
mycur = myconn.cursor()

# Step 4: Create table (only if it doesn't exist)
mycur.execute(
    """
CREATE TABLE IF NOT EXISTS students (
    sid VARCHAR(20) PRIMARY KEY,
    sname VARCHAR(25),
    age INT(10)
)
"""
)
print("Table created successfully")

# Step 5: Insert values using try-except to avoid duplicates
try:
    mycur.execute("INSERT INTO students VALUES ('501', 'ABC', 23)")
    mycur.execute("INSERT INTO students VALUES ('502', 'XYZ', 22)")
    myconn.commit()
    print("Data inserted successfully")
except mysql.connector.IntegrityError:
    print("Data already exists. Skipping insertion.")

# Step 6: Fetch and display all records
mycur.execute("SELECT * FROM students")
result = mycur.fetchall()
print("Student Details are:")
for x in result:
    print(x)

# Step 7: Update a record
mycur.execute("UPDATE students SET sname='Kumar' WHERE sid='502'")
myconn.commit()
print("Data updated successfully")

# Step 8
