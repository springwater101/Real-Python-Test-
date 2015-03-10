# import modules
import sqlite3
import random

# create and connect to a new db
with sqlite3.connect('newnum.db') as connection:
	cursor = connection.cursor()
	# the drop table command is used delete the table if exists
	cursor.execute("DROP TABLE if exists numbers")
	# creates a table called numbers with a column name num and takes int
	cursor.execute("""CREATE TABLE numbers(num INT)""")
	# loop 100 times
	for i in range(100):
		# inserts random numbers into the numbers table
		cursor.execute("INSERT INTO numbers VALUES(?)", (random.randint(0,100),))

	cursor.execute("SELECT * FROM numbers")

	rows = cursor.fetchall()

	for r in rows:
		print r[0]


	
