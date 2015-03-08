# SQLite Functions

import sqlite3

with sqlite3.connect("new.db") as connection:
	cursor = connection.cursor()
	# create a dictonary of sql querries
	sql = {'average':'SELECT avg(population) FROM population',
		'maximum': 'SELECT max(population) FROM population',
		'minimum': 'SELECT min(population) FROM population',
		'sum': 'SELECT sum(population) FROM population',
		'count': 'SELECT count(city) FROM population'}

	# run each sql query item in the dictionary
	for keys, values in sql.iteritems():
		# run sql
		cursor.execute(values)

		# fetchone() retrieves one record from the  query
		results = cursor.fetchone()
		# output theresults to screen
		print keys + ":", results[0]