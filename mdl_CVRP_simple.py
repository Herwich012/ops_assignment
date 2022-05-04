import numpy as np
from docplex.mp.model import Model
from geopy import distance #conda install -c conda-forge geopy
import fcs
import data

#%%Select data
OAK = fcs.aploc(data.OAKhub)
AWF = fcs.aploc(data.AFWhub_mini)

#%%Model parameters
rnd = np.random
rnd.seed(0)
n = len(AWF)-1                  #number of clients
Q = 1000                          #capacity of each vehicle
N = [i for i in range(1, n+1)]
V = [0] + N
q = {i: rnd.randint(1,10) for i in N}

A = [(i,j) for i in V for j in V if i != j] #arcs
c = {(i,j): round(distance.distance(AWF[i,1:3],AWF[j,1:3]).km,2) for i,j in A} #cost (distance)
#%%Model Constraints and Solving
mdl = Model('CVRP') #create the model
    
x = mdl.binary_var_dict(A, name='x') #variables x are binary, use binary format to keep amount variables low
u = mdl.continuous_var_dict(N, ub=Q, name='u')

mdl.minimize(mdl.sum(c[i, j]*x[i,j] for i, j in A)) #objective funtion
mdl.add_constraints(mdl.sum(x[i,j] for j in V if j != i) == 1 for i in N) #all nodes must be visited once
mdl.add_constraints(mdl.sum(x[i,j] for i in V if i != j) == 1 for j in N) #all nodes must be exited once

#indicator constraints are only enforced if a condition is met: if x[i,j]=1 then u[j] is etc..
mdl.add_indicator_constraints(mdl.indicator_constraint(x[i,j], u[i]+q[j] == u[j]) for i,j in A if i !=0 and j !=0)
mdl.add_constraints(u[i]>=q[i] for i in N)
mdl.parameters.timelimit = 5
solution = mdl.solve(log_output=True)

print(solution)
print(solution.solve_status)

active_arcs = [a for a in A if x[a].solution_value > 0.9]

#%% Plotting
fcs.solplot(AWF,active_arcs)