#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 12:13:21 2017

@author: janusboandersen
"""

import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#constants
a = 20  #harvesting [onyx / year]

k = 0.20  #instantaneous rate % of population growth [1/year]


#starting condition
y0 = a/k - 1
c1 = y0 - a/k  #arbitrary constant that can be calculated from starting conditions

#solution to the ODE
#if y0 = a/k there is an equilibrium solution / constant solution

def y(t):
    return a/k + c1 * math.exp(k*t)
    

#generate dataframe for plotting
data = pd.DataFrame(columns=("time", "y(t)"))

index_time = enumerate(list(np.linspace(0, 50, 101)), 1)

for i,t in index_time:
    data.loc[i] = t, y(t)
#end for


data.plot.line(x='time', y='y(t)');


#Extirpation, when y(t)=0, for a decaying population if y0 < a/k
if y0 < (a/k):
    decay = (-1) / (y0 * (k/a) - 1)
    te = (1/k) * math.log(decay)
    print("Decaying population, extirpation at t=",round(te,2));

#Equilibrium
elif y0 == (a/k):
    print("Equilibrium population and parameters.");

else:
    print("Population at exponential growth.");

