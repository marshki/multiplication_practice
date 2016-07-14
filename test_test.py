#!/bin/py
while True: 
	try:
		number = int(input('Pick a number in range 1-12 >>> '))
	except ValueError:
		print("That\'s not an int!")
		continue 
	else: 
		if not (1<= number <=12): 
			print('Not in range!')
			continue 
		else: 
			print('You selected:',number)
			break 
