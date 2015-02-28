# Create a SQLite3 database and table

# import sqlite3 library
import sqlite3

# Create a new databaase if the database dosen't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE popultaion
	(city TEXT, state TEXT, popultaion INT)
		""")

# close the database connection
conn.close()

