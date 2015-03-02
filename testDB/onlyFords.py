# Output only Ford cars

# Import sqlite3
import sqlite3

with sqlite3.connect("cars.db") as connection:
	cursor = connection.cursor()
	cursor.execute("SELECT make, model, quantity FROM inventory WHERE make = 'Ford'" )
	rows = cursor.fetchall()
	for r in rows:
		print r[0],r[1],r[2]