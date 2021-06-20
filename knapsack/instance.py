##### knapsack instance: put here the instance data

# Items
# item i -> {p: profit, w: weight}
# IMPORTANT: the i of the items starts from 1
O = {
	1: {"p": 1, "w":2},
	2: {"p": 2, "w":4},
	3: {"p": 2, "w":3},
	4: {"p": 3, "w":5}
}

# total number of items
n = len(O)

# max capacity of knapsack
b = 5
#####