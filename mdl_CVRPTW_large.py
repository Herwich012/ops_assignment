# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:37:53 2020

@author: Admin
"""

import numpy as np
from docplex.mp.model import Model
from geopy import distance #conda install -c conda-forge geopy
import fcs
import data

#%%Select data
OAK = fcs.aploc(data.OAKhub)
AWF = fcs.aploc(data.AFWhub_s)    #fcs.aploc(data.MEMDENhub_s)

#%%Model parameters
rnd = np.random
rnd.seed(0)
n = len(AWF)-2                         #number of clients
Q = 10000                                #capacity of each vehicle
N = [i for i in range(2, n+2)]         # Set of Customers
V = [0,1] + N                          # Nodes
q = {i: rnd.randint(1,10) for i in N}  # Demand of customer i
P = {i:0.5 for i in V}                 # Processing time of customer i
e = {i:rnd.randint(0,21) for i in V}   # Lower bound of time window
l = {i:e[i]+5 for i in V}              # Upper bound of time window
fc = 1000                               # fixed cost

A = [(i,j) for i in V for j in V if i != j] #arcs
c = {(i,j): round(distance.distance(AWF[i,1:3],AWF[j,1:3]).km,2) for i,j in A} #cost (distance)
t = {(i,j): round(distance.distance(AWF[i,1:3],AWF[j,1:3]).km/850,2) for i,j in A} # travel time

#%%Model Constraints and Solving
mdl = Model('CVRP') #create the model

x = mdl.binary_var_dict(A, name='x') #variables x are binary, use binary format to keep amount variables low
u = mdl.continuous_var_dict(N, ub=Q, name='u')      #   Variable that stores cargo amount
tau = mdl.continuous_var_dict(V, name='tau')        #   Decision variable for start of service time


mdl.minimize(mdl.sum(c[i, j]*x[i,j] for i, j in A) + mdl.sum(fc*x[0,j] for j in N) + mdl.sum(fc*x[1,j] for j in N)) #objective funtion
mdl.add_constraints(mdl.sum(x[i,j] for j in V if j != i) == 1 for i in N) #all nodes must be visited once
mdl.add_constraints(mdl.sum(x[i,j] for i in V if i != j) == 1 for j in N) #all nodes must be exited once
mdl.add_constraints(tau[i] >= e[i] for i in N)  # Time window Lower bound constraint
mdl.add_constraints(tau[i] <= l[i] for i in N)  # Time window upper bound constraint
mdl.add_constraints(u[i]>=q[i] for i in N)      # Lower bound constraint for capacity

#indicator constraints are only enforced if a condition is met: if x[i,j]=1 then u[j] is etc..
mdl.add_indicator_constraints(mdl.indicator_constraint(x[i,j], u[i]+q[j] == u[j]) for i,j in A if i !=0 and i !=1 and j !=0 and j !=1)
mdl.add_indicator_constraints(mdl.indicator_constraint(x[i, j], tau[j] >= tau[i] + P[i] + t[i,j]) for i, j in A if i != 0 and i !=1 and j !=0 and j != 1)

mdl.parameters.timelimit = 5
solution = mdl.solve(log_output=True)

print(solution)
print(solution.solve_status)

active_arcs = [a for a in A if x[a].solution_value > 0.9]

#%% Plotting
fcs.solplottw(AWF,active_arcs,e,l,tau)