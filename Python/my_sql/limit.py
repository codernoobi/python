import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")				#Select the 5 first records in the "customers" table using limit
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")		#Start from position 3, and return 5 records
myresult = mycursor.fetchall()
for x in myresult:
  print(x)