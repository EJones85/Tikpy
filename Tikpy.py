#!/usr/bin/python

import MySQLdb
import sys

def dbconnect(host, user, password, database):
	"""
	Function to allow connection to database for tickets, this will also check the
	DB credentials and give you an error when your credentials don't work.
	"""
	try:
		con = MySQLdb.connect(host, user, password, database)
		return con
	except MySQLdb.Error, E:
		print("Error {0}: {1}".format(E.args[0], E.args[1]))
		print("Entered wrong credentials for the database.")
		sys.exit(1)
		
class Tikpy(object):
	def __init__(self, host, user, password, database):
		self.host = host
		self.user = user
		self.password = password
		self.database = database

	def write(self):
		""" STDIN -> NONE
		Function to open a new ticket in the database, only asking for the description and setting
		the ticket status to OPN and assuming all other values.
		"""
		status = "OPN"
		description = raw_input("Describe the issue: ")
		con = dbconnect(self.host, self.user, self.password, self.database)
		with con:
			cur = con.cursor()
			cur.execute("INSERT INTO ticket VALUES(NULL, NULL, 1, '{0}', '{1}', NULL) ".format(status, description))
			cur.execute("SELECT * FROM ticket ORDER BY ID DESC LIMIT 1")
			result = cur.fetchone()
			print("ID     TIME                    UID   STATUS  DESCRIPTION") 
			print("{0}     {1}     {2}     {3}     {4}").format(result[0], result[1], result[2], result[3], result[4])
		if con:
			con.close()	

	def update(self, modtype):
		""" STDIN -> NONE
		Function to update the ticket, this will either close the ticket asking for a solution or
		modify the description of the ticket by adding additional information. It requires a
		predefined STR from the menu function to tell how this function should proceed.
		"""
		con = dbconnect(self.host, self.user, self.password, self.database)
		if modtype == 'close':
			ID = raw_input("What is the ticket number: ")
			solution = raw_input("How did you solve the issue?: ")
			with con:
				cur = con.cursor()
				cur.execute("UPDATE ticket SET Status='CLD', Solution='{0}' WHERE ID='{1}'".format(solution, ID))
			if con:
				con.close()

		elif modtype == 'modify':
			ID = raw_input("What is the ticket number: ")
			if ID.isdigit():
				description = raw_input("What would you like to add?: ")
				with con:
					cur = con.cursor()
					cur.execute("SELECT Description FROM ticket WHERE ID ='{0}'".format(ID))
					old_desc = cur.fetchone()
					cur.execute("UPDATE ticket SET Description='{0} Addition():{1}' WHERE ID='{2}'".format(old_desc[0], description, ID))
				if con:
					con.close()
			else:
				print("Error 7331: wrong input")

	def select(self, search_type):
		""" STDIN -> NONE
		Function to search the database for certain predefined values based on the STR passed
		by the menu function. This will search for open, closed, ticket number, and a date range 
		of tickets.
		"""
		con = dbconnect(self.host, self.user, self.password, self.database)
		if search_type == 'open':
			with con:
				cur = con.cursor(MySQLdb.cursors.DictCursor)
				cur.execute("SELECT ID, Description, Date, UID FROM ticket WHERE Status = 'OPN'")
				result = cur.fetchall()
				print("ID    UID   Description")
				for x in result:
					print("{0}     {1}     {2}".format(x["ID"], x["UID"], x["Description"][:35]))
			if con:
				con.close()

		if search_type == 'closed':
			with con:
				cur = con.cursor(MySQLdb.cursors.DictCursor)
				cur.execute("SELECT * FROM ticket WHERE Status = 'CLD'")
				result = cur.fetchall()
				print("ID    UID   Description")
				for x in result:
					print("{0}     {1}     {2}".format(x["ID"], x["UID"], x["Description"][:35]))
			if con:
				con.close()

		if search_type == 'ticket':
			search_value = raw_input("What is the ticket number: ")
			with con:
				cur = con.cursor(MySQLdb.cursors.DictCursor)
				cur.execute("SELECT * FROM ticket WHERE ID = {0}".format(search_value))
				result = cur.fetchall()
				print("ID    Status    UID   Description")
				for x in result:
					print("{0}     {1}       {2}     {3}".format(x["ID"], x["Status"], x["UID"], x["Description"][:35]))
			if con:
				con.close()

		if search_type == 'date':
			search_value = raw_input("Put in the date you are searching for")
			with con:
				cur = con.cursor(MySQLdb.cursors.DictCursor)
				cur.execute("SELECT * FROM ticket WHERE Status = 'CLD'")
				result = cur.fetchall()
				for x in result:
					print(x)
			if con:
				con.close()

		if search_type == 'word':
			search_value = raw_input("What Word(s) are you looking for: ")
			with con:
				cur = con.cursor(MySQLdb.cursors.DictCursor)
				cur.execute("SELECT * FROM ticket WHERE Description LIKE '%{0}%'".format(search_value))
				result = cur.fetchall()
				print("ID    Status    UID   Description")
				for x in result:
					print("{0}     {1}       {2}     {3}".format(x["ID"], x["Status"], x["UID"], x["Description"][:35]))
			if con:
				con.close()
