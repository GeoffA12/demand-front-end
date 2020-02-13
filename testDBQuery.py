import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='ShinyNatu34', database='team22demand')

cursor = mariadb_connection.cursor()

testUser = "geoff"

cursor.execute("SELECT username FROM customers")

rows = cursor.fetchall()
username_list = [x[0] for x in rows]
# check all usernames in the table to make sure we're keeping our usernames unique
userAlreadyExists = False
for x in username_list:
	print(x)
	if (testUser == x):
		userAlreadyExists = True
		break

response = None
# We'll send a 401 code back to the client if the user hasn't registered in our database
if (userAlreadyExists):
	response = 200
else:
	response = 401 
print(response)

#self.send_response(response)
