import sqlite3
import csv

with sqlite3.connect("cars.db") as connection:
	cursor = connection.cursor()
	cars = csv.reader(open("FordHonda.csv", "rU"))
	cursor.executemany("INSERT INTO inventory(make, model, quantity) values (?, ?, ?)", cars)

	