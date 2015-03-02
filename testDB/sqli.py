# Executemany() method

import sqlite3

with sqlite3.connect("new.db") as connection:

	cursor = connection.cursor()
	# insert multiple records using a tuple
	# (you can conpy paste the values)
	cities = [('Boston', 'MA', 600000),
		('Los Angeles', 'CA', 38000000),
		('Houston', 'TX', 2100000),
		('Philadelphia', 'PA', 1500000),
		('San Diego', 'TX', 130000),
		('San Antonio', 'TX', 1400000),
		('Dallas', 'TX', 1200000),
		('San Jose','CA', 900000),
		('jacksonville', 'IN', 800000),
		('Indianapolis', 'IN',800000),
		('Austin', 'TX', 800000),
		('Detroit', 'MI', 700000)
		]

	cursor.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)

	cursor.execute("SELECT * FROM population WHERE population > 1000000")

	rows = cursor.fetchall()

	for r in rows:
		print r[0], r[1], r[2]