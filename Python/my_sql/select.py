import mysql.connector				

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")				#Select all records from the "customers" table
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

mycursor.execute("SELECT name, address FROM customers")			#Select only the name and address columns
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

mycursor.execute("SELECT * FROM customers")				#Fetch only one row using fetchone()
myresult = mycursor.fetchone()
print(myresult)