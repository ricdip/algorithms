import libknapsack as lk
from instance import O, n, b


def print_instance(O, n, b):
	for k in O.keys():
		print(" item {} -> p: {} w: {}".format(k, O[k]["p"], O[k]["w"]))

	print()
	print(" (num items)    n = {}".format(n))
	print(" (tot capacity) b = {}".format(b))


def main():
	knapsack = lk.Knapsack(O, n, b)
	knapsack_dual = lk.KnapsackDual(O, n, b, standard_upperbound_p=True)

	print("\n***** knapsack instance *****")
	print()
	print_instance(O, n, b)

	print("\n\n\n***** progr-dyn-knapsack *****")

	# calculate knapsack solution with progr-dyn-knapsack: O(n * b) pseudo-polynomial time complexity
	m_k = knapsack.progr_dyn_knapsack()
	items_k = knapsack.items_in_sol()

	#print()
	#print(" Knapsack instance:\n")
	#knapsack.print_instance()
	print()
	print(' M:')
	knapsack.print_matrix(tabbed=True)
	print()
	print(' m = {}'.format(m_k))
	print()
	print(' items in solution: {}'.format(items_k))


	print("\n\n\n***** progr-dyn-knapsack-dual *****")

	# calculate knapsack solution with progr-dyn-knapsack-dual: O(n^2 * p_max) pseudo-polynomial time complexity
	m_kd = knapsack_dual.progr_dyn_knapsack_dual()
	items_kd = knapsack_dual.items_in_sol()

	#print()
	#print(" Knapsack instance:\n")
	#knapsack_dual.print_instance()
	print()
	print(' V:')
	knapsack_dual.print_matrix(tabbed=True)
	print()
	print(' m = {}'.format(m_kd))
	print()
	print(' items in solution: {}'.format(items_kd))


if __name__ == '__main__':
	main()