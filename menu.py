#!/usr/bin/python


MENU = {"Tickets":["Open Ticket", "Close Ticket", "Modify Ticket"], "Search":["Open Tickets", "Closed Tickets", "Ticket Numbers"]}

def menu_main(MNU):
	print("1.{0}\n2.{1}\n".format(*MNU.keys()))
	sel = raw_input("Selection:")
	if str(sel) not in "12":
		print "Select a Number between 1 and 2 please."
	elif not sel:
		exit()
	else:
		return str(sel)

def selection():
	sel = raw_input("> ")
	if sel not in "123":
		print("Select a Number between 1 and 3 please.")
	elif not sel:
		exit()
	else:
		return str(sel)

def menu_tickets(MNU):
	print("")
	print("Tickets Menu:")
	print("1.{0}   2.{1}   3.{2}".format(*MNU["Tickets"]))
	print("")
	selection()

def menu_search(MNU):
	print("")
	print("Search Menu:")
	print("1.{0}   2.{1}   3.{2}".format(*MNU["Search"]))
	print("")
	selection()


while True:
	print("")
	print("Welcome to Tikpy, a simple python ticketing system; please select from the following menu")
	print ""
	select = menu_main(MENU)
	if select == "1":
		menu_tickets(MENU)
	elif select == "2":
		menu_search(MENU)
	else:
		print("Error Wrong Input")
