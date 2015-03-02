# Home work
import sqlite3

with sqlite3.connect("cars.db") as connection:

	cursor = connection.cursor()

	cursor.execute("""CREATE TABLE orders(make TEXT, model TEXT, order_date TEXT)""")
	#cursor.execute("""CREATE TABLE regions(city TEXT, region TEXT)""")
	car_order = [('Ford', 'Fairlane', '2015-02-03'), ('Ford', 'Fairlane', '2015-02-04'), ('Ford', 'Fairlane', '2015-01-03'),
		('Ford', 'Cobra', '2015-01-29'), ('Ford', 'Cobra', '2015-01-25'),('Ford', 'Cobra', '2015-02-29'),
		('Ford', 'Falcon', '2015-01-04'), ('Ford', 'Falcon', '2015-01-05'), ('Ford', 'Falcon', '2015-01-08'),
		('Honda', 'Acclaim', '2014-12-04'),('Honda', 'Acclaim', '2015-03-04'),('Honda', 'Acclaim', '2014-11-11'),
		('Honda', 'Mini', '2014-12-04'), ('Honda', 'Mini', '2015-01-04'), ('Honda', 'Mini', '2015-02-10')]

	#cursor.executemany("INSERT INTO inventory(make, model, quantity) values (?, ?, ?)", cars)
	cursor.executemany("INSERT INTO orders(make, model, order_date) values (?, ?, ?)", car_order)

	cursor.execute("SELECT * FROM orders")
	rows = cursor.fetchall()
	for r in rows:
		print r[0], r[1],r[2]
