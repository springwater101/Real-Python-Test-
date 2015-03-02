# Joining data from multiple tables

import sqlite3

with sqlite3.connect("new.db") as connections:
	cursor = connections.cursor()
	# retrieve data
	cursor.execute("""SELECT population.city, population.population,
		regions.region FROM population, regions WHERE population.city = regions.city""")

	rows = cursor.fetchall()

	for r in rows:
		print r[0], r[1], r[2]