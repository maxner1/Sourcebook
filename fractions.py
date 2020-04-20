from __future__ import print_function
from reference import *
import random

# MIDEAST 341
# Matthew Axner (maxner)
# Interdisciplinary Project 2
# Ancient Egyptian Mathematical Sourcebook

# reference document for sourcebook.py

def study_frac():
	print("\nThe arithmetic behind fractions in ancient Egypt was similar to that as whole numbers.")
	print("However, the notation of these partial numbers was very unique to these people, and made some evidence appear quite convoluted.")
	print("The most common fractions-- and also the four for which they had unique heiroglyphs-- are 1/2, 1/3, 1/4, and 2/3.")
	print("To denote all other fractions, they took the combination of these four that got them as close to a sum of their")
	print("target fraction, followed by whatever smaller \"filler\" fractions finished the sum.")
	print("These \"filler\" fractions were always in the form 1/x.\n")

	print("Let's take a look at this example, which divides 40 by 2 1/2.\n")

	print(".\t2 1/2\n~10\t25\n~2\t5\n~4\t10\n_____________\nTotal\t40")
	print("The answer is 16, because the rows of 10, 2, and 4 summed to 40.\n")

	print("Here's another example, which multiplies 9/10 by 10:")
	print("Note that 9/10 is denoted 2/3 1/5 1/30, following the algorithm stated above.\n")

	print(".\t2/3 1/5 1/30\n~2\t1 2/3 1/10 1/30\n4\t3 1/2 1/10\n~8\t7 1/5\n_____________\nTotal\t9")
	print("The answer of 9 was obtained by adding 1 2/3 1/10 1/30 and 7 1/5.\n")

def gen_frac_mult():
	multiplier = random.randrange(0, 10, 1) # range: 1/10 -> 9 9/10 by 10ths
	mult_denom = random.randrange(2, 10, 1)
	mult_num = random.randrange(1, mult_denom, 1)
	multiplicand = random.randrange(2, 10, 1) # range: 2 -> 10 by 1s

	answer_whole = -1
	while (answer_whole == -1):
		print("\nWhat is " + str(multiplier) + " " + str(mult_num) + "/" + str(mult_denom) + " times " + str(multiplicand) + "?")
		answer_whole = int(raw_input("Enter your answer's whole number (or -1 for 2/N Table): "))
		if (answer_whole == -1):
			print_2N_table()
	answer_num = int(raw_input("Enter your answer's numerator: "))
	answer_denom = int(raw_input("Enter your answer's denominator: "))

	if ((answer_whole + (answer_num / float(answer_denom))) == ((multiplier + (mult_num / float(mult_denom))) * multiplicand)):
		return True
	else:
		return False

def gen_frac_div():
	divisor = (random.randrange(10, 100, 10)) # range: 100 -> 1000 by 10s
	possible_dividends = []
	poss_numers = []
	poss_denoms = []
	for i in range(1, 10):
		for j in range(2, 10):
			denom = j
			numer = 1
			if (denom != 2):
				numer = random.randrange(1, denom, 1)
			if (divisor / float(i + (numer / float(denom))) % 1 == 0):
				possible_dividends.append(i)
				poss_numers.append(numer)
				poss_denoms.append(denom)

	num = random.randrange(0, len(possible_dividends), 1)
	dividend = possible_dividends[num] # range: 1 -> 10 by possible factors
	dividend_numer = poss_numers[num]
	divident_denom = poss_denoms[num]

	answer = -1
	while (answer == -1):
		print("\nWhat is " + str(divisor) + " divided by " + str(dividend) + " " + str(dividend_numer) + "/" + str(divident_denom) + "?")
		answer = int(raw_input("Enter your answer (or -1 for 2/N Table): "))
		if (answer == -1):
			print_2N_table()

	if (answer == (divisor / float(dividend + (dividend_numer / float(divident_denom))))):
		return True
	else:
		return False

def practice_frac():
	print("Let's practice some fractions!")

	points = 0

	c = True
	while(c):
		md = random.randrange(0, 2, 1)
		correct = False
		if (md == 0):
			correct = gen_frac_mult()
		else:
			correct = gen_frac_div()

		if (correct):
			print("\nCorrect! You've been awarded 10 points!\n")
			points += 10
		else:
			print("\nSorry, that's incorrect.\n")

		c = cont()

	return points

def quiz_frac(passed_before):
	print("Quiz time! You must answer 3 correctly to pass the Fractions topic.")

	m_count = 0
	d_count = 0
	score = 0
	for i in range(0, 5):
		r = random.randrange(0, 2, 1)
		if (m_count < 3 and (r == 0 or d_count == 3)):
			m_count += 1
			correct = gen_frac_mult()

			if (correct):
				score += 1

		elif (r == 1 or m_count == 3):
			d_count += 1
			correct = gen_frac_div()

			if (correct):
				score += 1
	
	if (score >= 3):
		print(("\nCongrats! You scored " + str(score) + "/5"), end='')
		if not passed_before:
			print(" and passed this topic. You earned the Fractions badge!")
			return True
		else:
			print(" and passed this quiz.")
	else:
		print("Sorry, you did not pass this quiz. Try again!")
	return False