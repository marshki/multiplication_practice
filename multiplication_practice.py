#!/bin/py
#Python 3.4.3

# Import Python libraries 
import random	# for pseudo-random number generation 
from time import localtime, mktime	# for time tracker 

# Set time limit 
time_limit = 10 

# Initialize problem count, current score 
count, right= 0, 0 

# Welcome screen 
print("""
********************** Multiplication Tables **********************
This program allows you to practice multiplication facts from 1-12. 

You can answer each question by typing in your response and pressing 
the Enter key. To receive credit, you'll need to answer each 
question correctly within %d seconds. 

Press the 'q' key at anytime to quit.
""" % (time_limit,)) 

# Guts of the program 
input("Are you ready to play? Press the Enter key to begin. ") # Ask user to start program 
print()

while True: 
	count += 1

	a = random.randint(1,12) # Generate two (a,b) pseudo-random factors 
	b = random.randint(1,12) # between 1 and 12, inclusive 
	c =  a * b		 # Multiply the two factors, assign the product (c)	

	problem = "%d x %d = " % (a, b) # Assign problem
	correct_answer = c 		# Assign correct answer
	
	start_time = mktime(localtime())			# Start timer  
	user_answer = input("%3d.	" % count + problem)    # Wait for user input 
	end_time = mktime(localtime())				# End timer 

	if user_answer.lower() == 'q': # End loop when user wants to quit 
		count -= 1 	       # Reduce count by one if user exits program 
		break 

	if end_time - start_time > time_limit: # If too long, answer is marked as wrong 
		print ("You took too long!")
		continue
 
	try: 
		if int(user_answer) == correct_answer: # Compare user input with correct answer 
			right +=1		       # Assign point for correct answer  
			print("		Right-O!!!")
		else: 
			print("		Sorry, that\'s not right.")
			print("		%s%d" % (problem, correct_answer))

	except:						# Non integer answer are considered incorrect  
		print("		%s?	%s%d" % (user_answer, problem, correct_answer)) 


print ("\n	You answered %d correct out of %d." % (right, count)), # Show final score 
if right == count: 						       # Recognize perfect score 
	print("WOW. Awesome!")

