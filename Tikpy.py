#!/usr/bin/python

import MySQLdb

def dbconnect(host, user, password, database):
	con = MySQLdb.connect(host, user, password, database)
	return con

class Tikpy(object):
	def __init__(self):
		pass

	def write(self):
		status = "OPN"
		description = raw_input("Describe the issue: ")

		con = dbconnect('localhost', 'root', 'root', 'tikpy')
		with con:
			cur = con.cursor()
			cur.execute("INSERT INTO Ticket VALUES(NULL, NULL, 1, '%s', '%s', NULL) " 
			% (status, description))

		if con:
			con.close()
		

	def update(self, modtype):
		con = dbconnect('localhost', 'root', 'root', 'tikpy')
		if modtype == 'close':
			ID = raw_input("What is the ticket number: ")
			solution = raw_input("How did you solve the issue?: ")
			with con:
				cur = con.cursor()
				cur.execute("UPDATE Ticket SET Status='CLD', Solution='%s' WHERE ID='%s'" 
				% (solution, ID))

			if con:
				con.close()

		elif modtype == 'modify':
			ID = raw_input("What is the ticket number: ")
			description = raw_input("What would you like to add?: ")
			with con:
				cur = con.cursor()
				cur.execute("SELECT Description FROM Ticket WHERE ID ='%s'" 
				% (ID))
				old_desc = cur.fetchone()
				cur.execute("UPDATE Ticket SET Description='%s Addition():%s' WHERE ID='%s'" 
				% (old_desc[0], description, ID))

			if con:
				con.close()

	def select(self, search_type):
		con = dbconnect('localhost', 'root', 'root', 'tikpy')
		if search_type == 'open':
			with con:
				cur = con.cursor(MySQLdb.cursors.DictCursor)
				cur.execute("SELECT * FROM Ticket WHERE Status = 'OPN'")
				result = cur.fetchall()
				for x in result:
					print x

			if con:
				con.close()

		if search_type == 'closed':
			with con:
				cur = con.cursor(MySQLdb.cursors.DictCursor)
				cur.execute("SELECT * FROM Ticket WHERE Status = 'CLD'")
				result = cur.fetchall()
				for x in result:
					print x

			if con:
				con.close()

		if search_type == 'ticket':
			search_value = raw_input("What is the ticket number: ")
			with con:
				cur = con.cursor(MySQLdb.cursors.DictCursor)
				cur.execute("SELECT * FROM Ticket WHERE ID = %s" % search_value)
				result = cur.fetchall()
				for x in result:
					print x
			if con:
				con.close()

		if search_type == 'date':
			search_value = raw_input("Put in the date you are searching for")
			with con:
				cur = con.cursor(MySQLdb.cursors.DictCursor)
				cur.execute("SELECT * FROM Ticket WHERE Status = 'CLD'")
				result = cur.fetchall()
				for x in result:
					print x
			if con:
				con.close()

test = Tikpy()
test.select('ticket')
