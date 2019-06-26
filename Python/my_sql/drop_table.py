import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"		#Delete the table "customers"
mycursor.execute(sql)

sql = "DROP TABLE IF EXISTS customers"		#Delete the table "customers" if it exists
mycursor.execute(sql)