import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"			#Delete any record where the address is "Mountain 21"
mycursor.execute(sql)
mydb.commit()											#Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
print(mycursor.rowcount, "record(s) deleted")			# The WHERE clause specifies which record(s) that should be deleted. If you omit the WHERE clause, all records will be deleted!

"""
It is considered a good practice to escape the values of any query, also in delete statements.
This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
The mysql.connector module uses the placeholder %s to escape values in the delete statement
"""
sql = "DELETE FROM customers WHERE address = %s"			#Escape values by using the placeholder %s method
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")