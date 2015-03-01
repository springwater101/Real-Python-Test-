# import sqlite3
import sqlite3

# Create a new databaase if the database dosen't already exist
conn = sqlite3.connect("cars.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE inventory(make TEXT, model TEXT, quantity INT)""")

# close the database connection
conn.close()