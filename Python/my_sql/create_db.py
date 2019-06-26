import mysql.connector

mydb = mysql.connector.connect(					
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")			#create a database named "mydatabase"


mycursor.execute("SHOW DATABASES")			#Return a list of your system's databases
for x in mycursor:
  print(x)

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"								#connecting to mydatabase
)