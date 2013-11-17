#!/usr/bin/python

import MySQLdb

def dbconnect(host, user, password, database):
	con = MySQLdb.connect(host, user, password, database)
	return con

class Tikpy(object):
	def __init__(self):
		pass

	def write(self):
		""" STDIN -> NONE
		Function to open a new ticket in the database, only asking for the description and setting
		the ticket status to OPN and assuming all other values.
		"""
		status = "OPN"
		description = raw_input("Describe the issue: ")
		con = dbconnect('localhost', 'root', 'root', 'tikpy')
		with con:
			cur = con.cursor()
			cur.execute("INSERT INTO Ticket VALUES(NULL, NULL, 1, '{0}', '{1}', NULL) ".format(status, description))
			cur.execute("SELECT * FROM Ticket ORDER BY ID DESC LIMIT 1")
			result = cur.fetchone()
			print(result)
		if con:
			con.close()	

	def update(self, modtype):
		""" STDIN -> NONE
		Function to update the ticket, this will either close the ticket asking for a solution or
		modify the description of the ticket by adding additional information. It requires a
		predefined STR from the menu function to tell how this function should proceed.
		"""
		con = dbconnect('localhost', 'root', 'root', 'tikpy')
		if modtype == 'close':
			ID = raw_input("What is the ticket number: ")
			solution = raw_input("How did you solve the issue?: ")
			with con:
				cur = con.cursor()
				cur.execute("UPDATE Ticket SET Status='CLD', Solution='{0}' WHERE ID='{1}'".format(solution, ID))
			if con:
				con.close()

		elif modtype == 'modify':
			ID = raw_input("What is the ticket number: ")
			description = raw_input("What would you like to add?: ")
			with con:
				cur = con.cursor()
				cur.execute("SELECT Description FROM Ticket WHERE ID ='{0}'".format(ID))
				old_desc = cur.fetchone()
				cur.execute("UPDATE Ticket SET Description='{0} Addition():{1}' WHERE ID='{2}'".format(old_desc[0], description, ID))
			if con:
				con.close()

	def select(self, search_type):
		""" STDIN -> NONE
		Function to search the database for certain predefined values based on the STR passed
		by the menu function. This will search for open, closed, ticket number, and a date range 
		of tickets.
		"""
		con = dbconnect('localhost', 'root', 'root', 'tikpy')
		if search_type == 'open':
			with con:
				cur = con.cursor(MySQLdb.cursors.DictCursor)
				cur.execute("SELECT ID, Description, Date, UID FROM Ticket WHERE Status = 'OPN'")
				result = cur.fetchall()
				for x in result:
					print(x)
			if con:
				con.close()

		if search_type == 'closed':
			with con:
				cur = con.cursor(MySQLdb.cursors.DictCursor)
				cur.execute("SELECT * FROM Ticket WHERE Status = 'CLD'")
				result = cur.fetchall()
				for x in result:
					print(x)
			if con:
				con.close()

		if search_type == 'ticket':
			search_value = raw_input("What is the ticket number: ")
			with con:
				cur = con.cursor(MySQLdb.cursors.DictCursor)
				cur.execute("SELECT * FROM Ticket WHERE ID = %s" % search_value)
				result = cur.fetchall()
				for x in result:
					print(x)
			if con:
				con.close()

		if search_type == 'date':
			search_value = raw_input("Put in the date you are searching for")
			with con:
				cur = con.cursor(MySQLdb.cursors.DictCursor)
				cur.execute("SELECT * FROM Ticket WHERE Status = 'CLD'")
				result = cur.fetchall()
				for x in result:
					print(x)
			if con:
				con.close()

test = Tikpy()
test.write()
