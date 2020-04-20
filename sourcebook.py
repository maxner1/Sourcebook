from __future__ import print_function
import random
from multiplication_and_division import *
from fractions import *
from algebra import *
from geometry import *
from units_of_measurement import *

# MIDEAST 341
# Matthew Axner (maxner)
# Interdisciplinary Project 2
# Ancient Egyptian Mathematical Sourcebook

# RUN ME LIKE THIS: $ python sourcebook.py

"""
Assignment:

Based on examples of Mesopotamian and Egyptian mathematical texts, create a source book of mathematical problems 
that you would use to teach key Egyptian or Mesopotamian mathematical principles. The source book should include 
at least 10 problems of a variety of different types and while the problems should be based on exemplars from 
ancient sources, they should not be identical (i.e. use different numbers) to extant problems. Also include at 
least one reference list (this should be identical to an ancient exemplar) that must be consulted to solve one 
of the problems. In addition, write a 2-3 pg reflection on the key principles that are included in your source 
book and why they are relevant. You should take on the persona of an ancient scribe, but you may imagine your 
audience to either be ancient students or modern ones.

Details: 

This is a menu-based Python program which will serve as an educational reference on ancient Egyptian mathematics. 
Users will have the choice between learning, practicing, and quizzing various mathematical principles. 
Reference lists will be provided when necessary. 
Practice and quizzes will provide you with a score, and awards will be available upon certain achievements. 

Concepts:
 - Multiplication / Division
 - Fractions
 - Algebra
 - Geometry
 - Special! Pyramids and Rations

References:
 - 2 / N Table
 - Measurements Table

"""

class User:
	name = "Djehudymose"
	points = 0
	badges = []

user = User()

def print_progress():
	print("\nYour Progress:\n")

	print("User:\t" + user.name)
	print("Points:\t" + str(user.points))
	print("Badges:", end="")
	if (len(user.badges) == 0):
		print("\tNone :(")
	for badge in user.badges:
		print("\t" +  badge)


def main():

	print("Welcome to Ancient Egyptian Mathematical Sourcebook!\n")

	print("Let's start with your name.")
	user.name = raw_input("What would you like to call yourself? ")

	print("\nNice to meet you, " + user.name + ".\n")

	print("Ready to get started?")

	run()

	print("\nThanks for using Ancient Egyptian Mathematical Sourcebook!")

def run():
	done = False
	while not done:
		print("\nHow would you like to get learning?")
		print("\t1: Study\n\t2. Practice\n\t3. Quiz\n\t4. See progress\n\t5. Exit")
		choice = (int)(raw_input("Enter your choice (1-4): "))

		topic = 0
		if (choice >= 1 and choice <= 3):
			while (topic < 1 or topic > 6):
				print("\nWhat topic would you like to cover?")
				print("\t1. Multiplication and Division\n\t2. Fractions\n\t3. Algebra\n\t4. Geometry\n\t5. Units of Measurement\n\t6. Back")

				topic = (int)(raw_input("Enter your choice (1-6): "))
				if (topic < 1 or topic > 6):
					print("\nERROR: Invalid input!")

		elif (choice < 1 or choice > 5):
			print("\nERROR: Invalid input!\n")

		# Study
		if (choice == 1):
			# Multiplication/Division
			if (topic == 1):
				study_md()
			# Fractions
			elif (topic == 2):
				study_frac()
			# Algebra
			elif (topic == 3):
				study_alg()
			# Geometry
			elif (topic == 4):
				study_geo()
			#Pyramids and Rations
			elif (topic == 5):
				study_units()

		# Practice
		elif (choice == 2):
			# Multiplication/Division
			if (topic == 1):
				user.points += practice_md()
			# Fractions
			elif (topic == 2):
				user.points += practice_frac()
			# Algebra
			elif (topic == 3):
				user.points += practice_alg()
			# Geometry
			elif (topic == 4):
				user.points += practice_geo()
			#Pyramids and Rations
			elif (topic == 5):
				user.points += practice_units()

		# Quiz
		elif (choice == 3):
			passed = False
			# Multiplication/Division
			if (topic == 1):
				passed_before = False
				for b in user.badges:
					if (b == "Multiplication and Division"):
						passed_before = True
				passed = quiz_md(passed_before)
				if (passed):
					user.badges.append("Multiplication and Division")
			# Fractions
			elif (topic == 2):
				passed_before = False
				for b in user.badges:
					if (b == "Fractions"):
						passed_before = True
				passed = quiz_frac(passed_before)
				if (passed):
					user.badges.append("Fractions")
			# Algebra
			elif (topic == 3):
				passed_before = False
				for b in user.badges:
					if (b == "Algebra"):
						passed_before = True
				passed = quiz_alg(passed_before)
				if (passed):
					user.badges.append("Algebra")
			# Geometry
			elif (topic == 4):
				passed_before = False
				for b in user.badges:
					if (b == "Geometry"):
						passed_before = True
				passed = quiz_geo(passed_before)
				if (passed):
					user.badges.append("Geometry")
			#Pyramids and Rations
			elif (topic == 5):
				passed_before = False
				for b in user.badges:
					if (b == "Units of Measurement"):
						passed_before = True
				passed = quiz_units(passed_before)
				if (passed):
					user.badges.append("Units of Measurement")

		elif (choice == 4):
			print_progress()
		# Exit
		elif (choice == 5):
			done = True

main()






















