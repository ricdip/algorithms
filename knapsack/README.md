# Max 0-1 Knapsack algorithms

A possible Python implementation of some algorithms that solve the Max 0-1 Knapsack problem.

The algorithms' pseudocodes were seen in the Web algorithms course at the University of L'Aquila.

## Algorithms

- **progr-dyn-knapsack**: algorithm that solve the problem with the dynamic programming approach. It has a pseudo-polynomial time complexity O(n * b)

    where:
    - n is the number of items
    - b is the total capacity of the knapsack

- **progr-dyn-knapsack-dual**: algorithm that solve the dual problem with the dynamic programming approach. It has a pseudo-polynomial time complexity O(n^2 * p_max)

    where:
    - n is the number of items
    - p_max is the maximum profit between all items

## Requirements

- [numpy](https://pypi.org/project/numpy/) Python library installed via pip

## Execution

1. open instance.py and write the Knapsack instance data there
2. create Python venv: ```make install```
3. solve the instance: ```make run```

## Output

The output are the filled table used for the execution, the set of the selected items in the optimal solution and the measure of the optimal solution m for the algorithms.
