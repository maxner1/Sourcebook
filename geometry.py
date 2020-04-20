from __future__ import print_function
from reference import *
import random

# MIDEAST 341
# Matthew Axner (maxner)
# Interdisciplinary Project 2
# Ancient Egyptian Mathematical Sourcebook

# reference document for sourcebook.py

def study_geo():
	print("\nThe first interesting subtopic of ancient Egyptian geometry was their calculations for circles.")
	print("What's significant about this is that the ancients hadn't created the concept of pi (3.14159...) quite yet.")
	print("However, the Egyptians were particularly good at estimating measurements of a circle. For areas of a circle,")
	print("they would subtract 1/diameter from the diameter, and square the resulting quanitity to find the area.\n")

	print("Take a look at this example, which finds the area of a circle of diameter 13.\n")

	print("Method of calculating a circular area of 13.")
	print("What is its amount as area?")
	print("You shall subtract its 1/13 as 1, while the remainder is 12.")
	print("You shall multiply 12 times 12.")
	print("It shall result as 144.")
	print("Its amount as area: 144.\n")

	print("Calculation how it results, circular area of 13:")
	print(".\t13\nits /13\t1")
	print("Subtraction from it, remainder 12.\n")

	print(".\t12\n2\t24\n~4\t48\n~8\t96")
	print("\nIts amount as area: 144.\n")

	print("Another common subtopic was the calculation of the volume of a truncated pyramid.")
	print("While the ancient Egyptians did not have an actual term for this object, it was denoted with a symbol (shaped like a trapezoid).")
	print("Their method for doing so took the squared length of its upper and lower sides and added these with the double of the lower.")
	print("Next, they multiplied this by the third of the height to find the volume.")
	print("This equivilates to today's forumula of 1/3 * (a^2 + ab + b^2) * h.\n")

	print("See the process in the following example, which takes a truncated pyramid with lower side 5, upper side 3, and height 12.\n")

	print("You shall square these 5. 25 shall result.")
	print("You shall square these 3. 9 shall result.")
	print("You shall triple 5. 15 shall result.")
	print("You shall add the 25 and 9 and 15. 49 shall result.")
	print("You shall calculated 1/3 of 12. 4 shall result.")
	print("Look, beloinging to you is 196.\n")

	print("3, squared 9\n---\n|   \\\n|    \\\n|     \\\t\t1/3 4\t.\t49\n|      \\\t\t2\t98\n|       \\\t\t4\t196\n|        \\\n|         \\")
	print("-----------\n5, squared 25\n.\t5\n2\t10\n_____________\nTotal\t15")

def gen_circ():
	diameter = random.randrange(5, 26, 1) # 5 <= diameter <= 25

	answer = -1
	while (answer == -1):
		print("\nAccording to ancient Egyptian arithmetic, what is the area of a circle with diameter " + str(diameter) + "?")
		answer = int(raw_input("Enter your answer (or -1 for 2/N Table): "))
		if (answer == -1):
			print_2N_table()

	if (answer == ((diameter - 1) * (diameter - 1))):
		return True
	else:
		return False

def gen_pyr():
	lower = random.randrange(4, 10, 1) # 5 <= lower <= 9
	upper = random.randrange(2, 5, 1) # 2 <= upper <= 4
	height = random.randrange(3, 31, 3) # 3 <= height <= 30, by 3s

	answer = -1
	while (answer == -1):
		print("\nAccording to ancient Egyptian arithmetic, what is the volume of a truncated pyramid with the following:")
		print("Lower edge " + str(lower) + ", upper edge " + str(upper) + ", height " + str(height))
		answer = int(raw_input("Enter your answer (or -1 for 2/N Table): "))
		if (answer == -1):
			print_2N_table()

	if (answer == (height / float(3)) * (lower * lower + lower * upper + upper * upper)):
		return True
	else:
		return False

def practice_geo():
	print("Let's practice some geometry!")

	points = 0

	c = True
	while(c):
		cp = random.randrange(0, 2, 1)
		correct = False
		if (cp == 0):
			correct = gen_circ()
		else:
			correct = gen_pyr()

		if (correct):
			print("\nCorrect! You've been awarded 10 points!\n")
			points += 10
		else:
			print("\nSorry, that's incorrect.\n")

		c = cont()

	return points

def quiz_geo(passed_before):
	print("Quiz time! You must answer 3 correctly to pass the Geometry topic.")

	c_count = 0
	p_count = 0
	score = 0
	for i in range(0, 5):
		r = random.randrange(0, 2, 1)
		if (c_count < 3 and (r == 0 or p_count == 3)):
			c_count += 1
			correct = gen_circ()

			if (correct):
				score += 1

		elif (r == 1 or c_count == 3):
			p_count += 1
			correct = gen_pyr()

			if (correct):
				score += 1
	
	if (score >= 3):
		print(("\nCongrats! You scored " + str(score) + "/5"), end='')
		if not passed_before:
			print(" and passed this topic. You earned the Geometry badge!")
			return True
		else:
			print(" and passed this quiz.")
	else:
		print("Sorry, you did not pass this quiz. Try again!")
	return False