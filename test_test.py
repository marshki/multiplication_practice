#!/bin/py
number = 0 
while True: 
	try:
		number = int(input("Enter a whole number between 1 and 12 >>> "))
	except ValueError:
		print("Invlaid input, please try again >>> ")
		continue 
	else: 
		if not (1<= number <=12):
			print("Need a whole number in range 1-12 >>> ") 
			continue 
		else: 
			print("You selected:",number)
			break 
