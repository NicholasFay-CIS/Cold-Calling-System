"""
Group 2
2/3/2020
Majed Almazrouei, Justin Becker, Dylan Conway, Kyle Diodati, Nicholas Fay
"""
#imported lib
from random import *

class Randomizer:
	'''
	This class is intended to create a list of which order the students will be picked.
	Afterwards it can be used to reshuffle the queue of students or to check randomness of the ordering.
	'''
	def __init__(self, count=0):
		'''
		initializes the random class to how many students are in class, sets seed of randomization,
		and creates a list in which the order of students will be saved.
		'''
		self.size = count
		seed()
		self.order = list()
		self.randomize()

	def set_size(self, count=0):
		self.size = count
		return
    
	def randomize(self):
		'''
		None -> None
		creates a randomize ordering of students
		'''
		temp = list()

		self.verify() #verifies the seed is good for randomization and changes if needed

		i=0
		while i < self.size:
			temp.append(i)
			i += 1
		self.order = sample(temp, k=self.size)

		return

	def randomize_back(self, index):
		'''
		None -> None
		creates a randomize ordering of back of students
		'''
		temp = list()
		size = index

		self.verify() #verifies the seed is good for randomization and changes if needed

		while index < self.size:
			temp.append(index)
			index += 1
		self.order = sample(temp, k=self.size - size)

		return

	def verify(self):
		'''
		None -> None
		Tests randomization to see if the seed is randomized enough
		'''
		total = 0 #holds the sum of all random integers
		totalstd = 0 #holds the sum of all std deviations
		
		lst = list() #list of all random integer choices

		i=0
		while i < 100: #picks 100 random integers
			curr = randint(1,100)
			total += curr
			lst.append(curr)
			i += 1
		avg = total / 100

		for index in lst: #calculates standard deviation of each random choice
			curr = abs(avg - index)
			totalstd += curr
		avgstd = totalstd / 100

		if (avgstd < 10): #if the standard deviation is not varied enough, reset seed and re-verify
			seed()
			print("Randomization Verification: Failed")
			print("Reattempting Verification With New Seed")
			self.verify()
		else:
			print("Randomization Verification: Passed")
			return

	def verification_check(self):
		'''
		None -> Bool
		Can be used to manually see if the randomization is varied enough at any point
		'''
		total = 0 #holds the sum of all random integers
		totalstd = 0 #holds the sum of all std deviations
		
		lst = list() #list of all random integer choices

		i=0
		while i < 100: #picks 100 random integers
			curr = randint(1,100)
			total += curr
			lst.append(curr)
			i += 1
		avg = total / 100

		for index in lst: #calculates standard deviation of each random choice
			curr = abs(avg - index)
			totalstd += curr
		avgstd = totalstd / 100

		if (avgstd > 10): #if the standard deviation is varied enough return true, else it is false
			print("Randomization Verification: Passed")
			return True
		return False
		print("Randomization Verification: Failed")
