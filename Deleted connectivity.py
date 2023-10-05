import mysql.connector as c
con=c.connect(host="localhost", user="root", password="Kushagra*123", database="record")

cursor=con.cursor()
last_name = 'Smith'
query = "delete from students where last_name = '{}'".format(last_name)
cursor.execute(query)
con.commit()
print("Executed Succesfully")
