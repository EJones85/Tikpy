#!/usr/bin/python

import Tikpy

Tik = Tikpy.Tikpy()

MENU = {"Tickets":["Open Ticket", "Close Ticket", "Modify Ticket"], "Search":["Open Tickets", "Closed Tickets", "Ticket Numbers"]}
EXQT = ["exit", "quit", "close", "Exit", "Quit", "Close"]
BACK = ["back", "b", "B", "Back", "previous", "p", "P", "Previous"]

def menu_main(MNU):
	print("1.{0}   2.{1}".format(*MNU.keys()))
	sel = raw_input("> ")
	if not sel or sel in EXQT:
		exit()
	elif sel not in "12":
		print("1 or 2 please.")	
	else:
		return str(sel)

def selection():
	count = 0
	while count < 3:
		sel = raw_input("> ")
		if sel in BACK:
			break
		elif sel in EXQT:
			exit()
		elif sel not in "123":
			count += 1	
		else:
			return str(sel)

def menu_opt(men_return):
	print("")
	if men_return == "1":
		print("Tickets Menu:")
		print("1.{0}   2.{1}   3.{2}".format(*MENU["Tickets"]))
		var = selection()
		if var == "1":
			Tik.write()
		elif var == "2":
			Tik.update('close')
		elif var == "3":
			Tik.update('modify')
		else:
			print "Error 43"
	elif men_return == "2":
		print("Search Menu:")
		print("1.{0}   2.{1}   3.{2}".format(*MENU["Search"]))
		var = selection()
		if var == "1":
			Tik.select("open")
		elif var == "2":
			Tik.select("closed")
		elif var == "3":
			Tik.select("ticket")
		else:
			print "Error 44"
	else:
		print("Error 42")

if __name__ == "__main__":
		while True:
			print("")
			print("Welcome to Tikpy, a simple python ticketing system; please select from the following menu:")
			print("")
			MENU1 = menu_main(MENU)
			menu_opt(MENU1)
