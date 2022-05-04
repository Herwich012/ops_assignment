# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 14:41:03 2022

@author: hajo__000
"""

import numpy as np
from docplex.mp.model import Model
from geopy import distance #conda install -c conda-forge geopy
import fcs
import data
from itertools import permutations

#%%Model parameters
AWF = fcs.aploc(data.AFWhub_mini)

rnd = np.random
rnd.seed(0)
n = len(AWF)-1                  #number of clients
Q = 1000                          #capacity of each vehicle
N = [i for i in range(1, n+1)]
V = [0] + N
q = {i: rnd.randint(1,10) for i in N}

A = [(i,j) for i in V for j in V if i != j] #arcs
c = {(i,j): round(distance.distance(AWF[i,1:3],AWF[j,1:3]).km,2) for i,j in A} #cost (distance)

client_paths = list(permutations(range(1,7)))
costs = []
for i in client_paths:
    path = (0,) + i + (0,)
    path_cost = 0
    for j in range(len(path)-1):
        path_cost = path_cost + c[(path[j],path[j+1])]
        
    costs.append(path_cost)

min_cost = min(costs)
shortest_index = min(range(len(costs)), key=costs.__getitem__)
shortest_path = (0,) + client_paths[shortest_index] + (0,)
