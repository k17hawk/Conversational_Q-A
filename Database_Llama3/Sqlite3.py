import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("student.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the STUDENT table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
"""
cursor.execute(table_info)

# Insert two rows into the STUDENT table
insert_query = """
INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)
"""
students = [
    ("John Doe", "Data Science", "A", 85),
    ("Jane Smith", "Data Engineer", "B", 90),
    ("Mark Evan", "Data Engineer", "B", 60),
    ("John Cena", "Data Engineer", "B", 80),
    ("Tim Smith", "DEVOPS", "A", 90),
    ("Millon ane", "Data Science", "A", 80),
    ("Kim Kardasian", "Sociology", "B", 40),
    ("Hary potter", "Mystic", "A", 90)
]

cursor.executemany(insert_query, students)

# Commit the changes
connection.commit()

print("The student datas are:")
data = cursor.execute(''' Select * from STUDENT''')
for row in data:
    print(row)
# Close the connection
connection.close()
