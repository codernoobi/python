import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"			#Sort the result alphabetically by name
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

sql = "SELECT * FROM customers ORDER BY name DESC"			#Sort the result reverse alphabetically by name using DESC
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)