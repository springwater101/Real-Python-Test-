import sqlite3

with sqlite3.connect("cars.db") as connection:
	cursor = connection.cursor()
	cursor.execute("""SELECT DISTINCT from inventory.make, inventory.model,inventory.quantity,
		orders.order_date FROM inventory, orders WHERE inventory.model = orders.model""")

	#cursor.execute("""SELECT DISTINCT population.city, population.population,
		#regions.region FROM population, regions WHERE
		#population.city = regions.city ORDER by population.city ASC""")

	rows = cursor.fetchall()

	for r in rows:
		print "Model: " + [0]
		print "Make: " + [1]
		print "QTY: " + [2]
		print "Orders: " + [3]

