# UPDATING THE CARS .DB and printing the results to screen

# Import sqlite3
import sqlite3

with sqlite3.connect("cars.db") as connection:
	cursor = connection.cursor()
	# update data
	cursor.execute("UPDATE inventory SET quantity = 10 WHERE model =' Fairlane'")
	cursor.execute("UPDATE inventory SET quantity = 2 WHERE model =' Mini'")

	print "\nNEW DATA:\n"

	cursor.execute("SELECT * FROM inventory")

	rows  = cursor.fetchall()

	for r in rows:
		print r[0], r[1], r[2]