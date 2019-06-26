import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"			#Overwrite the address column from "Valley 345" to "Canyoun 123"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

sql = "UPDATE customers SET address = %s WHERE address = %s"				#prevent sql injection
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")