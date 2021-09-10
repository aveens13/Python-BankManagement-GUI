

import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ronaldo@345",
    database="bankmanagement"
)
my_cursor = db.cursor()
my_cursor.execute("SELECT balance FROM Details1 WHERE name='Sulav'")
val = my_cursor.fetchall()
print(val[0][0])
db.close()