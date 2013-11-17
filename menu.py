#!/usr/bin/python

import Tikpy

Tik = Tikpy.Tikpy()

MENU = {"Tickets":["Open Ticket", "Close Ticket", "Modify Ticket"], "Search":["Open Tickets", "Closed Tickets", "Ticket Numbers"]}
EXQT = ["exit", "quit", "close", "Exit", "Quit", "Close", "EXIT", "QUIT", "CLOSE", "e", "q", "c", "E", "Q", "C"]
BACK = ["back", "b", "B", "Back", "previous", "p", "P", "Previous"]
TIK_MEN = [x for x in MENU["Tickets"]]
SCH_MEN = [x for x in MENU["Search"]]

def menu_main(MNU):
	""" STDIN > STR
	Menu function for top level menu:
	valid selecitons 1, 2 will exit if no input is given or input from EXQT list is given
	"""
	print("1.{0}   2.{1}".format(*MNU.keys()))
	sel = raw_input("> ")
	if not sel or sel in EXQT:
		exit()
	elif sel not in "12":
		print("1 or 2 please.")	
	else:
		return str(sel)

def selection(sel_list):
	""" STDIN > STR
	Selection function for sub menus tickets and search checks input between 1 and menu list
	length. Will exit if input is in EXQT, or if input is wrong 3 times will go back to
	main menu
	"""
	count = 0
	while count < 3:
		sel = raw_input("> ")
		if sel in BACK:
			break
		elif sel in EXQT:
			exit()
		elif sel not in [str(x) for x in range(1,len(sel_list) + 1)]:
			count += 1	
		else:
			return str(sel)

def menu_opt(men_return):
	""" STDIN > None
	This is a menu option function that performs a call on the Tikpy module to edit the 
	backend database based on the user selection. Takes input from main_menu function.
	"""
	print("")
	if men_return == "1":
		print("Tickets Menu:")
		print("1.{0}   2.{1}   3.{2}".format(*MENU["Tickets"]))
		var = selection(TIK_MEN)
		if var == "1":
			Tik.write()
		elif var == "2":
			Tik.update('close')
		elif var == "3":
			Tik.update('modify')
		else:
			print("Error in Ticket menu function in menu_opt function.")
	elif men_return == "2":
		print("Search Menu:")
		print("1.{0}   2.{1}   3.{2}".format(*MENU["Search"]))
		var = selection(SCH_MEN)
		if var == "1":
			Tik.select("open")
		elif var == "2":
			Tik.select("closed")
		elif var == "3":
			Tik.select("ticket")
		else:
			print("Error 44")
	else:
		print("Error in Search menu function in menu_opt function.")

if __name__ == "__main__":
		while True:
			print("")
			print("Welcome to Tikpy, a simple python ticketing system; please select from the following menu:")
			print("")
			MENU1 = menu_main(MENU)
			menu_opt(MENU1)
