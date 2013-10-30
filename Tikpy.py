#!/usr/bin/python

import MySQLdb

def dbconnect(host, user, password, database):
	con = MySQLdb.connect(host, user, password, database)
	return con

class Tikpy(object):
	def __init__(self, status, description, solution, uid="uid"):
		self.status = status
		self.description = description
		self.solution = solution
		self.uid = uid

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
		

	def update(self, status, solution):
		pass
	def select(self):
		pass

test = Tikpy("OPN", "Test", "Test")
test.write()
