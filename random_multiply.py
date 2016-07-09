#!/bin/bash 
import random
from time import localtime, mktime 

def random_multiply():
	''' Blah Blah Blah  
	'''
	# Set time limit 
	time_limit= 10 
	
	# Initialize problem count, current score 
	count, right= 0, 0 
	
	print('''
	You can answer each question by typing in your response and pressing the Enter key. 
	To receive credit, you'll need to answer each question correctly within %d seconds.
	Press the 'q' key at anytime to quit.
	''' % (time_limit,))

	input("	Are you ready to play? For a GOOD time press then Enter key. ") # Ask user to start program 
	print()
	
	while True: 
		count += 1

		a = random.randint(1,12)	# Generate two (a,b) pseudo-random numbers
		b = random.randint(1,12)	# between 1 and 12, inclusive 
		c = a * b 			# multiply the two numbers, assign the product (c)

		problem = "%d x %d = " % (a, b) 	# Assign problem 
		correct_answer = c 			# Assign correct answer 
	
		start_time = mktime(localtime())			# Start timer 
		user_answer = input("	%3d.	" % count + problem)	# Wait for user input 
		end_time = mktime(localtime())				# End timer 
	
		if user_answer.lower() == 'q':	# End loop when user wants to quit 
			count -= 1		# Reduce count by one if the user exits program 
			break 
		
		if end_time - start_time > time_limit: 				# If too long, answer is marked as wrong 
			print("			You took too long!")
			print("		%s%d" % (problem, correct_answer))	# Provide correct answer
			continue 
	
		try: 
			if int(user_answer) == correct_answer: # Compare user input with the correct answer 
				right +=1		       # Assign point for correct answer 
				print("			Right-O!!!")
			else: 
				print("			Sorry, that\'s not right.")
				print("		%s%d" % (problem, correct_answer)) # Provide correct answer
		
		except:						# Non-integer answers are considered incorrect 
			print("			%s?" % (user_answer,)) 
			print("		%s%d" % (problem, correct_answer))
		
	print("\n	You answered %d correct out of %d." % (right, count)), # Show final score

	percent = round(right/count * 100.0) if count else 0		       # Calculate percent correct  
	
	print("	That\'s %d%%." % (percent,)),
	
	if right == count and right >= 1: 				       # Recognize a perfect score 
		print("	WOW. Awesome!!!")
()

random_multiply()
