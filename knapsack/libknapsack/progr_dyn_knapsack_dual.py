import numpy as np


class KnapsackDual:
	def __init__(self, O, n, b, standard_upperbound_p=True):
		self.O = O
		self.n = n
		self.b = b
		self.p_max = self.get_p_max(self.O)

		if standard_upperbound_p:
			self.P = self.n * self.p_max
		else:
			self.P = sum([self.O[i]["p"] for i in self.O.keys()])
		
		self.V = np.empty((self.n+1,self.P+1), dtype=float)
		self.m = 0
		self.items = []


	# aux function to get the p_max from the Knapsack instance
	def get_p_max(self, O):
		p_m = 0
		for k in O.keys():
			if O[k]["p"] > p_m:
				p_m = O[k]["p"]
		return p_m
		

	# progr-dyn-knapsack-dual: pseudo-polynomial complexity O(n * P) = O(n^2 * p_max)
	def progr_dyn_knapsack_dual(self):
		# init row 0
		for p in range(0, self.P+1):
			self.V[0,p] = np.inf
		# init col 0
		for i in range(0, self.n+1):
			self.V[i,0] = np.inf

		for i in range(1, self.n+1):
			for p in range(1, self.P+1):
				if self.O[i]["p"] >= p:
					self.V[i,p] = min(self.V[i-1,p], self.O[i]["w"])
				else:
					self.V[i,p] = min(self.V[i-1,p], self.V[i-1,p - self.O[i]["p"]] + self.O[i]["w"])

		self.m = max([p for p in range(0,self.P+1) if self.V[self.n,p] <= self.b])
		return self.m


	def items_in_sol(self):
		self.items = []

		i = self.n
		k = self.m
		while i > 0 and k > 0:
			if self.V[i-1, k] > self.V[i, k]:
				self.items.append(i)
				k = k - self.O[i]["p"]
				i = i - 1
			else:
				i = i - 1

		return self.items


	def print_matrix(self, tabbed=True):
		for i in range(0,self.n+1):
			if tabbed:
				print("\t", end='')
			for j in range(0,self.P+1):
				if self.V[i,j] != np.inf:
					if digits(int(self.V[i,j])) < 2:
						print(" {}  ".format(int(self.V[i,j])), end='')
					else:
						# it's ok but if we have more than 2 digits it is surely unformatted
						print(" {} ".format(int(self.V[i,j])), end='')
				else:
					print(" {}  ".format("\u221E"), end='')
			print()


	def print_instance(self):
		print(" n = {}".format(self.n))
		print(" b = {}".format(self.b))
		print(" p_max = {}".format(self.p_max))
		print(" P = {}".format(self.P))
		print()
		for k in self.O.keys():
			print(" {} : {}".format(k, self.O[k]))


def digits(num):
	d = 0
	while num > 0:
		d = d + 1
		num = num // 10
	return d