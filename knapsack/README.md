# Dynamic programming examples for Max 0-1 Knapsack

A possible Python implementation of two algorithms that solve the Max 0-1 Knapsack problem with the dynamic programming approach.

Both algorithms' pseudocodes were seen in the Web algorithms course at the University of L'Aquila.

## Algorithms

- **progr-dyn-knapsack**: pseudo-polynomial time complexity c

    <img src="https://render.githubusercontent.com/render/math?math=c = O(n \cdot b)">

    where:
    - n is the number of items
    - b is the total capacity of the knapsack

- **progr-dyn-knapsack-dual**: pseudo-polynomial time complexity c

    <img src="https://render.githubusercontent.com/render/math?math=c = O(n^2 \cdot p_{max})">

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

The output are the filled table used for the execution, the set of the selected items in the optimal solution and the measure of the optimal solution m for both algorithms.
