#!/usr/bin/python

import MySQLdb

class Tikpy(object):
	def __init__(self):
		pass
	
	def dbconnect(self):
		c = MySQLdb.connect("localhost","root","root","Tikpy")
		return c

	def read(self):
		c = dbconnect()
		d = c.cursor
		
		if c:
			c.close()

	def write(self):
		pass

	def modify(self):
		pass

	def search(self):
		pass

if __name__ == '__main__':
	ticket = Tikpy()
	while True:
		print "Make a selection:"
		print "1. Create Ticket(s)"
		print "2. Modify Ticket(s)"
		print "3. Search Tickets"
		print "4. View Tickets"
		print "0. Exit"
		selection = raw_input("Make a Selection: ")
		
		if selection == '1':
			ticket.write()
		elif selection == '2':
			ticket.modify()
		elif selection == '3':
			ticket.search()
		elif selection == '4':
			pass
		elif selection == '0':
			break
		else:
			print "Invalid selection!"
