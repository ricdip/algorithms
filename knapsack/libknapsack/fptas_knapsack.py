import numpy as np
import math
from .progr_dyn_knapsack_dual import KnapsackDual


class FPTASKnapsack:
    def __init__(self, O, n, b, epsilon):
        self.epsilon = epsilon
        self.n = n
        self.b = b
        self.m = 0
        self.items = []

        self.p_max = self.get_p_max(O)
        self.k = self.calculate_k(self.epsilon, self.p_max, self.n)
        self.scaled_O = self.scale_O(O, self.k)

        self.kd = KnapsackDual(self.scaled_O, self.n, self.b, standard_upperbound_p=True)


    # aux function to get the p_max from the Knapsack instance
    def get_p_max(self, O):
            p_m = 0
            for k in O.keys():
                    if O[k]["p"] > p_m:
                            p_m = O[k]["p"]
            return p_m


    # k = floor((epsilon * p_max) / n)
    def calculate_k(self, epsilon, p_max, n):
        return math.floor((epsilon * p_max) / n)


    # scaling all items' profits: floor(p_i / k)
    def scale_O(self, O, k):
        if k == 0:
            raise RuntimeError("k = 0: it is not possible to run FPTAS-knapsack with this instance and epsilon")
        return {i: {"p": (math.floor(O[i]["p"] / k)), "w": O[i]["w"]} for i in O.keys()}


    def FPTAS_knapsack(self):
        # k = floor((epsilon * p_max) / n)

        # we use progr_dyn_knapsack_dual to find the optimal solution of the instance with scaled profits
        self.m = self.kd.progr_dyn_knapsack_dual()

        # we return the items return by progr_dyn_knapsack_dual
        self.items = self.kd.items_in_sol()

        return self.items

    
    def print_matrix(self, tabbed=True):
        self.kd.print_matrix(tabbed)


    def print_instance(self):
        print(" epsilon = {}".format(self.epsilon))
        print(" k = {}".format(self.k))
        self.kd.print_instance()
