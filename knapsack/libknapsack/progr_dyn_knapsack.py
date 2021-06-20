import numpy as np


class Knapsack:
	def __init__(self, O, n, b):
		self.O = O
		self.n = n
		self.b = b
		self.M = np.empty((self.n+1,self.b+1), dtype=int)
		self.m = 0
		self.items = []
		

	# progr-dyn-knapsack: pseudo-polynomial complexity O(n * b)
	def progr_dyn_knapsack(self):
		# init row 0
		for w in range(0, self.b+1):
			self.M[0,w] = 0
		# init col 0
		for i in range(0, self.n+1):
			self.M[i,0] = 0

		for i in range(1, self.n+1):
			for w in range(1, self.b+1):
				if self.O[i]["w"] > w:
					self.M[i,w] = self.M[i-1,w]
				else:
					self.M[i,w] = max(self.M[i-1,w], self.M[i-1,w - self.O[i]["w"]] + self.O[i]["p"])

		self.m = self.M[self.n,self.b]
		return self.m


	def items_in_sol(self):
		self.items = []
		
		i = self.n
		k = self.b
		while i > 0 and k > 0:
			if self.M[i-1, k] < self.M[i, k]:
				self.items.append(i)
				k = k - self.O[i]["w"]
				i = i - 1
			else:
				i = i - 1

		return self.items


	def print_matrix(self, tabbed=True):
		for i in range(0,self.n+1):
			if tabbed:
				print("\t", end='')
			for j in range(0,self.b+1):
				print(" {} ".format(self.M[i,j]), end='')
			print()


	def print_instance(self):
		print(" n = {}".format(self.n))
		print(" b = {}".format(self.b))
		print()
		for k in self.O.keys():
			print(" {} : {}".format(k, self.O[k]))
