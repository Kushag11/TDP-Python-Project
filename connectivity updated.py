import mysql.connector as c
con=c.connect(host="localhost", user="root", password="Kushagra*123", database="record")

cursor=con.cursor()
grade = 97
first_name = "Alice"
query="update students set grade = {} where first_name = '{}'".format(grade,first_name)
cursor.execute(query)
con.commit()
print("Data Updated successfully")
