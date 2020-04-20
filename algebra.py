from __future__ import print_function
from reference import *
import random

# MIDEAST 341
# Matthew Axner (maxner)
# Interdisciplinary Project 2
# Ancient Egyptian Mathematical Sourcebook

# reference document for sourcebook.py

def study_alg():
	print("\nAncient Egyptian algebra was performed using the same arithmetic as our algebra today.")
	print("The main differences to note are in the wording of the problem as well as how they went about solving it.")
	print("Problems were worded such that the quantity of interest (usually called \"x\") was noted as a set quantity rather than a variable.")
	print("More importantly, the process to solve was via reversing the problem from answer to quantity.\n")

	print("See the example below, which today would be seen as solving x + x/6 = 21.\n")

	print("A quanity, its /6 added to it so that 21 results.")
	print("Calculate with 6.")
	print("You shall calculate its /6 as 1. Total 7.")
	print("Divide 21 by 7.")
	print("~.\t7\n~2\t14\n\n_____________\nTotal\t21\n")
	print("3 shall result.")
	print("Multiply 3 by 6.")
	print(".\t3\n~2\t6\n~4\t12\n_____________\nTotal\t18")
	print("18 shall result.")
	print(".\t18\n/6\t3 Total 21")
	print("The quanitity 18, its /6, 3, total 21.\n")

	print("Note the ancient Egyptians ALWAYS checked their answers for problems like these.")

def gen_alg_mult():
	x = random.randrange(10, 26, 1) # 10 <= x <= 25
	pm = random.randrange(0, 2, 1)
	y = random.randrange(2, 6, 1) # 2 <= y <= 5

	answer = -1
	while (answer == -1):
		print("\nA quantity, its " + str(y) + " added to it so that " + str(x + x * y) + " results.")
		answer = int(raw_input("Enter your answer (or -1 for 2/N Table): "))
		if (answer == -1):
			print_2N_table()

	if (answer == x):
		return True
	else:
		return False

def gen_alg_div():
	x = 7
	while (prime(x)):
		x = random.randrange(10, 26, 1) # 10 <= x <= 25
	y = 26
	while ((x / float(y)) % 1 != 0):
		y = random.randrange(2, 6, 1) # 2 <= y <= 5

	pm = random.randrange(0, 2, 1)
	answer = -1
	while (answer == -1):
		if (pm == 0):
			print("\nA quantity, its /" + str(y) + " added to it so that " + str(int(x + (x / float(y)))) + " results.")
		else:
			print("\nA quantity, its /" + str(y) + " taken from it so that " + str(int(x - (x / float(y)))) + " results.")
		answer = int(raw_input("Enter your answer (or -1 for 2/N Table): "))
		if (answer == -1):
			print_2N_table()

	if (answer == x):
		return True
	else:
		return False

def practice_alg():
	print("Let's practice some algebra!")

	points = 0

	c = True
	while(c):
		md = random.randrange(0, 2, 1)
		correct = False
		if (md == 0):
			correct = gen_alg_mult()
		else:
			correct = gen_alg_div()

		if (correct):
			print("\nCorrect! You've been awarded 10 points!\n")
			points += 10
		else:
			print("\nSorry, that's incorrect.\n")

		c = cont()

	return points

def quiz_alg(passed_before):
	print("Quiz time! You must answer 3 correctly to pass the Algebra topic.")

	m_count = 0
	d_count = 0
	score = 0
	for i in range(0, 5):
		r = random.randrange(0, 2, 1)
		if (m_count < 3 and (r == 0 or d_count == 3)):
			m_count += 1
			correct = gen_alg_mult()

			if (correct):
				score += 1

		elif (r == 1 or m_count == 3):
			d_count += 1
			correct = gen_alg_div()

			if (correct):
				score += 1
	
	if (score >= 3):
		print(("\nCongrats! You scored " + str(score) + "/5"), end='')
		if not passed_before:
			print(" and passed this topic. You earned the Algebra badge!")
			return True
		else:
			print(" and passed this quiz.")
	else:
		print("Sorry, you did not pass this quiz. Try again!")
	return False