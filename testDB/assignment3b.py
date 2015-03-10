import sqlite3

with sqlite3.connect('newnum.db') as connection:
	cursor = connection.cursor()
	prompt="""
	Select the operation that you want to preform [1-5]:
	1. Average
	2. Max
	3. Min
	4. Sum
	5. Exit
	"""

	while True:
		# get user input
		x = raw_input(prompt)

		# if user enters any choice from 1-4
		if x in set(["1","2","3","4"]):
			# parse the corresponding operation text

			operation = {1:"avg",2:"max",3:"min",4:"sum"}[int(x)]

			#retrieve data
			cursor.execute("SELECT {}(num) from numbers".format(operation))
			get = cursor.fetchone()

			print operation + ": %f" % get[0]

		elif x == "5":
			print "Exit"
			break