import mysql.connector

mysql = mysql.connector.connect(host="localhost", port=6666, user="root", passwd="password")
mycursor = mysql.cursor()

mycursor.execute("show databases")

for name in mycursor:
    print(name)

mycursor.execute("select * from telusko.student")
result_set = mycursor.fetchall()
print('Print student names')
for student in result_set:
    print(student)
