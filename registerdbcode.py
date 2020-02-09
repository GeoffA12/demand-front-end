import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='ShinyNatu34', database='team22demand')
cursor = mariadb_connection.cursor()
newUser = "michaels"
newPassword = "We Are Very Safe"
newEmail = "email@email.com"
newPhone = "512-674-3333"

cursor.execute("SELECT username FROM customers")

rows = cursor.fetchall()
usernames = [x[0] for x in rows]

# Check if the username already exists in our customer database
userAlreadyExists = False
for x in usernames:
	if (newUser == x):
		userAlreadyExists = True

response = None
if (userAlreadyExists):
	response = 401
else:
	response = 200
	newCursor = mariadb_connection.cursor()
	newCursor.execute("INSERT INTO customers (username, password, email, phone) VALUES (%s, %s, %s, %s)", (newUser, newPassword, newEmail, newPhone))
	mariadb_connection.commit()
print(response)
# return self.response(response)





