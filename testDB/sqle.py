# INSERT Command with Error Handler

# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect('new.db')

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:
	# inset new data
	cursor.execute("INSERT INTO	populations VALUES('New York City', 'NY', 82000000)")
	cursor.execute("INSERT INTO populations VALUES('San Fancisco', 'CA', 8000000)")

	# commit
	conn.commit()
except sqlite3.OperationalError as e:
	print "OOps!,  Something went wrong. Try again..."
	print "error: %s" % e

#	close the database
conn.close()