import mysql.connector
conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
my_cursor = conn.cursor()

conn.commit()
conn.close()

print("Connection successfully created!")