import mysql.connector as c
con=c.connect(host="localhost", user="root", password="Kushagra*123", database="record")

cursor=con.cursor()
cursor.execute("select * from students")
data=cursor.fetchall()
print(data)
print("Executed Successfully")
