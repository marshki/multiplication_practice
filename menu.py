#!/bin/py 	
# Python 3.4.3 
# Made with <3 for RNK 

def menu():
	''' Print menu options and prompt user for input 
	'''
	print()
	print("What would you like to do?")
	print()
	print("1) I want to practice random multiplication facts.")
	print()
	print("2) I want to practice a single family of multiplication facts.")
	print() 
	print("3) I want to quit...for now!")
	print()
	return input("Please make your choice (1,2,3) then press Enter: ")
() 

# Program 
loop = 1 
choice = 0 
while loop == 1: 
	choice = menu()
	if choice == '1':
		print()
		print("OK! Let\'s practice random multiplication facts.")
	elif choice == '2': 
		print()
		print("Cool! Let\'s practice a single family of multiplication facts.")
	elif choice == '3':
		print()
		print("Y\'all come back now, ya hear?") 
		loop = 0 
	else: 
		print()
		print("*** Sorry, you must select a valid option (1,2,3), then press Enter. Try again. ***")
