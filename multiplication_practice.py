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
question correctly in %d seconds. 

Press the 'q' key at anytime to quit.
""" % (time_limit,)) 

input("Are you ready to play? Press the Enter key to begin. ")
print()

while True: 
	count += 1

# Generate two random factors (a, b), each between 1 and 12, inclusive
# Multiply the two factors and assign the product (c)  
	a = random.randint(1,12) 
	b = random.randint(1,12) 
	c =  a * b

# Assign problem, correct answer 
	problem = "%d x %d = " % (a, b)
	correct_answer = c 
	
# Track time 
# Prompt for user input 
	start_time = mktime(localtime())
	user_answer = input("%3d.	" % count + problem)
	end_time = mktime(localtime())

# End loop when user wants to quit 
	if user_answer.lower() == 'q':
		count -= 1 
		break 

# If too long, answer is marked as wrong 
	if end_time - start_time > time_limit: 
		print ("	You took too long!")
		continue 

# Compare user input with correct answer 
# Assign point for correct answer 
# If answer is not an integer, answer is considered incorrect 
	try: 
		if int(user_answer) == correct_answer: 
			right +=1 
			print("		Right-O!!!")
		else: 
			print("		Sorry, that\'s not right.")
			print("		%s%d" % (problem, correct_answer))

	except: 
		print("		%s?	%s%d" % (user_answer, problem, correct_answer))

# Show final score 
print ("\n	You answered %d correct out of %d." % (right, count)), 
if right == count: 
	print("Perfect!")

