from __future__ import print_function
from reference import *
import random

# MIDEAST 341
# Matthew Axner (maxner)
# Interdisciplinary Project 2
# Ancient Egyptian Mathematical Sourcebook

# reference document for sourcebook.py

def study_md():
	print("\nLet's start with some Multiplication.\n")

	print("To perform this operation, the ancient Egyptians would perform a series of repeated doubling and multiplying by 10 on the multiplier.")
	print("In doing, so they looked for a combination of numbers that summed to the multiplcand.")
	print("Once found, they added the total of the resultant numbers in these rows to find the product.\n")

	print("See the following example, which multiplies 400 by 5:\n")

	print("~.\t400\n2\t800\n~4\t1600\n_____________\nTotal\t2000")
	print("The answer is the sum of the resultant numbers. In this case, 2,000 + 8,000 = 10,000.\n")

	print("Now on to Division.\n")

	print("For division, the ancient Egyptians adopted a similar strategy to multiplication.")
	print("They looked for a combination of resulting numbers from the original process (as opposed to the numbers used) that summed to the divisor.")
	print("Once found, they added the total of the numbers used in these rows to find the quotient.\n")

	print("Here's an example, which divides 1120 by 80:\n")

	print(".\t80\n~10\t800\n2\t160\n~4\t320\n_____________\nTotal\t1120")
	print("The answer is the sum of the numbers used. In this case, 10 + 4 = 14.\n")

def gen_mult():
	multiplier = random.randrange(10, 100, 1) # range: 10 -> 100 by 1s
	multiplicand = random.randrange(2, 10, 1) # range: 2 -> 10 by 1s

	answer = -1
	while (answer == -1):
		print("\nWhat is " + str(multiplier) + " times " + str(multiplicand) + "?")
		answer = int(raw_input("Enter your answer (or -1 for 2/N Table): "))
		if (answer == -1):
			print_2N_table()

	if (answer == (multiplier * multiplicand)):
		return True
	else:
		return False

def gen_div():
	divisor = 7
	while (prime(divisor)):
		divisor = random.randrange(10, 100, 1) # range: 10 -> 100 by 1s
	possible_dividends = []
	for i in range(2, 10):
		if (divisor / float(i) % 1 == 0):
			possible_dividends.append(i)

	dividend = possible_dividends[random.randrange(0, len(possible_dividends), 1)] # range: 1 -> 10 by possible factors

	answer = -1
	while (answer == -1):
		print("\nWhat is " + str(divisor) + " divided by " + str(dividend) + "?")
		answer = int(raw_input("Enter your answer (or -1 for 2/N Table): "))
		if (answer == -1):
			print_2N_table()

	if (answer == (divisor / dividend)):
		return True
	else:
		return False

def practice_md():
	print("Let's practice some multiplication and division!")

	points = 0

	md = random.randrange(0, 2, 1)
	c = True
	while (c):
		if (md == 0):
			correct = gen_mult()

		else:
			correct = gen_div()

		#correct answer
		if (correct):
			print("\nCorrect! You've been awarded 10 points!\n")
			points += 10
		else:
			print("\nSorry, that's incorrect.\n")

		c = cont()
		md = random.randrange(0, 2, 1)

	return points

def quiz_md(passed_before):
	print("Quiz time! You must answer 3 correctly to pass the Multiplication and Division topic.")

	m_count = 0
	d_count = 0
	score = 0
	for i in range(0, 5):
		r = random.randrange(0, 2, 1)
		if (m_count < 3 and (r == 0 or d_count == 3)):
			m_count += 1
			correct = gen_mult()

			if (correct):
				score += 1

		elif (r == 1 or m_count == 3):
			d_count += 1
			correct = gen_div()

			if (correct):
				score += 1
	
	if (score >= 3):
		print(("\nCongrats! You scored " + str(score) + "/5"), end='')
		if not passed_before:
			print(" and passed this topic. You earned the Multiplication and Division badge!")
			return True
		else:
			print(" and passed this quiz.")
	else:
		print("Sorry, you did not pass this quiz. Try again!")
	return False