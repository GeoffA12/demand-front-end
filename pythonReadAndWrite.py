import mysql.connector as mariadb

# Setup the connection to our demand database
mariadb_connection = mariadb.connect(user='root', password='some_pass', database='team22demand')

# Cursor is an object which we'll use to execute our database read and writes
cursor = mariadb_connection.cursor()

# this is how we insert data into our table called 'test' 
newName = "Hello"
newPassword = "SafePassword"
cursor.execute("INSERT INTO test (username, password) VALUES (%s, %s)", (newName, newPassword))

# We can also read data from a query using the cursor.execute() command
cursor.execute("SELECT * from test")

# Print out all rows and columns of data in the test table
for x in cursor:
    print(x)
