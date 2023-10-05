import mysql.connector as c
con=c.connect(host="localhost", user="root", password="Kushagra*123", database="record")

cursor=con.cursor()
student_id = 1
first_name = "Alice"
last_name = "Smith"
age = 18
grade = 95.5

query = "insert into students values({},'{}','{}',{},{})".format(student_id,first_name,last_name,age,grade)
cursor.execute(query)
con.commit()
print("Data inserted Successfully")
