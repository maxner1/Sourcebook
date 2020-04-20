from __future__ import print_function
from reference import *
import random

# MIDEAST 341
# Matthew Axner (maxner)
# Interdisciplinary Project 2
# Ancient Egyptian Mathematical Sourcebook

# reference document for sourcebook.py

lengths = ["ht", "cubits", "palms", "digits"]
areas = ["ht-3t", "st3.t", "area-cubits"]
volumes = ["h3r", "hq3.t", "hnw", "r3"]

def print_measurement_table():
	print("Ancient Egyptian Measurents Table:\n")

	print("Length measures:")
	print("1 ht\t= 100 cubits\t(= ~52.5m)\n1 cubit\t= 7 palms\t(= ~52.5 cm)\n1 palm\t= 4 digits\t(= ~7.5 cm)\n1 digit\t\t\t(= ~ 19mm)\n")

	print("Area measures:")
	print("1 ht-3t\t\t=10 st3.t\t\t(= ~27562.2 sq. m)\n1 st3.t\t\t=1 area-cubits\t\t(= ~2756.25 sq. m)\n1 area-cubit\t\t(= ~27.56 sq. m)\n")

	print("Volume measures:")
	print("1 h3r\t= 16 hq3.t\t(= ~76.8 cube L)\n1 hq3.t\t= 10 hnw\t(= ~4.8 L)\n1 hnw\t= 32 r3\t\t(= ~0.48 L)\n1 r3\t\t\t(= ~15 mL)\n")	

def study_units():
	print("NOTE: This final topic will draw upon the Multiplication and Division topic and will begin using ancient Egyptian units of measurement.\n")

	print("The ancient Egyptian people had their own measurement system, with conversions not much less complicated than our Imperial system.")
	print("The following table notes common units of measurements, and their standard for converting:\n")

	print_measurement_table()

	print("That's all for this unit! This table will be made available to you in the unit practice and quiz.")

def get_conversion():
	typ = random.randrange(0, 4, 1)
	question_unit = ""
	answer_unit = ""
	conv = 0
	if (typ == 0):
		u = random.randrange(0, 4, 1)
		question_unit = lengths[u]
		pm = random.randrange(0, 2, 1)
		if (pm == 0 and u > 0):
			answer_unit = lengths[u - 1]
			if (u == 1):
				conv = 1 / float(100)
			elif (u == 2):
				conv = 1 / float(7)
			else:
				conv = 1/ float(4)
		elif (pm == 0 and u == 0):
			answer_unit = lengths[u + 1]
			conv = 100
		elif (pm == 1 and u < 3):
			answer_unit = lengths[u + 1]
			if (u == 0):
				conv = 100
			elif (u == 1):
				conv = 7
			else:
				conv = 4
		else:
			answer_unit = lengths[u - 1]
			conv = 1 / float(4)
	elif (typ == 1):
		u = random.randrange(0, 3, 1)
		question_unit = areas[u]
		pm = random.randrange(0, 2, 1)
		if (pm == 0 and u > 0):
			answer_unit = areas[u - 1]
			if (u == 1):
				conv = 1 / float(10)
			else:
				conv = 1 / float(100)
		elif (pm == 0 and u == 0):
			answer_unit = areas[u + 1]
			conv = 10
		elif (pm == 1 and u < 2):
			answer_unit = areas[u + 1]
			if (u == 0):
				conv = 10
			else:
				conv = 100
		else:
			answer_unit = areas[u - 1]
			conv = 1 / float(100)
	else:
		u = random.randrange(0, 4, 1)
		question_unit = volumes[u]
		pm = random.randrange(0, 2, 1)
		if (pm == 0 and u > 0):
			answer_unit = volumes[u - 1]
			if (u == 1):
				conv = 1 / float(16)
			elif (u == 2):
				conv = 1 / float(10)
			else:
				conv = 1/ float(32)
		elif (pm == 0 and u == 0):
			answer_unit = volumes[u + 1]
			conv = 16
		elif (pm == 1 and u < 3):
			answer_unit = volumes[u + 1]
			if (u == 0):
				conv = 16
			elif (u == 1):
				conv = 10
			else:
				conv = 32
		else:
			answer_unit = volumes[u - 1]
			conv = 1 / float(32)

	return conv, question_unit, answer_unit

def gen_unit_mult():
	multiplier = random.randrange(10, 100, 1) # range: 10 -> 100 by 1s
	multiplicand = random.randrange(2, 10, 1) # range: 2 -> 10 by 1s

	conv = get_conversion()

	answer = -1
	while (answer == -1):
		print("\nWhat is " + str(multiplier) + conv[1] + " times " + str(multiplicand) + "?")
		print("Express your answer in terms of " + conv[2] + ".")
		answer = int(raw_input("Enter the whole number of your answer (or -1 for 2/N Table, -2 for Measurements Table): "))
		if (answer == -1):
			print_2N_table()
		elif (answer == -2):
			print_measurement_table()

	if (answer == floor((multiplier * multiplicand) * conv[0])):
		return True
	else:
		return False

def gen_unit_div():
	divisor = 7
	while (prime(divisor)):
		divisor = random.randrange(10, 100, 1) # range: 10 -> 100 by 1s
	possible_dividends = []
	for i in range(2, 10):
		if (divisor / float(i) % 1 == 0):
			possible_dividends.append(i)

	dividend = possible_dividends[random.randrange(0, len(possible_dividends), 1)] # range: 1 -> 10 by possible factors

	conv = get_conversion()

	answer = -1
	while (answer == -1 or answer == -2):
		print("\nWhat is " + str(divisor) + conv[1] + " divided by " + str(dividend) + "?")
		print("Express your answer in terms of " + conv[2] + ".")
		answer = int(raw_input("Enter the whole number of your answer (or -1 for 2/N Table, -2 for Measurements Table): "))
		if (answer == -1):
			print_2N_table()
		elif (answer == -2):
			print_measurement_table()

	if (answer == floor((divisor / dividend) * conv[0])):
		return True
	else:
		return False

def practice_units():
	print("Let's practice some units!")

	points = 0

	c = True
	while(c):
		cp = random.randrange(0, 2, 1)
		correct = False
		if (cp == 0):
			correct = gen_unit_mult()
		else:
			correct = gen_unit_div()

		if (correct):
			print("\nCorrect! You've been awarded 10 points!\n")
			points += 10
		else:
			print("\nSorry, that's incorrect.\n")

		c = cont()

	return points

def quiz_units(passed_before):
	print("Quiz time! You must answer 3 correctly to pass the Units of Measurement topic.")

	m_count = 0
	d_count = 0
	score = 0
	for i in range(0, 5):
		r = random.randrange(0, 2, 1)
		if (m_count < 3 and (r == 0 or d_count == 3)):
			m_count += 1
			correct = gen_unit_mult()

			if (correct):
				score += 1

		elif (r == 1 or m_count == 3):
			d_count += 1
			correct = gen_unit_div()

			if (correct):
				score += 1
	
	if (score >= 3):
		print(("\nCongrats! You scored " + str(score) + "/5"), end='')
		if not passed_before:
			print(" and passed this topic. You earned the Units of Measurement badge!")
			return True
		else:
			print(" and passed this quiz.")
	else:
		print("Sorry, you did not pass this quiz. Try again!")
	return False