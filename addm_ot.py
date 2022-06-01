#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 22:17:44 2022

@author: floriskrijgsman
"""

from time import time
import numpy as np
import matplotlib.pyplot as plt
from phe import paillier
from ot import Alice, Bob
from random_number_generator_with_ot import random_number_generator

maxIter = 18
n = 3
rho = 1
public_key, private_key = paillier.generate_paillier_keypair()
timer = np.zeros([1,maxIter])
#x = np.zeros([n,maxIter])
x = []
u = []
print_x = []
q = np.ones((n))

avg = np.zeros([1,maxIter]) 
avg = [[public_key.encrypt(float(x)) for x in y] for y in avg][0] # Global variable must be encrypted

x.append([1, .3, .1])
print_x.append([1, .3, .1])
u.append([-1, -.3, -.1])

agent_1 = [print_x[0][0]]
agent_2 = [print_x[0][1]]
agent_3 = [print_x[0][2]]
t = [0]


r_1, r_2, r_3 = random_number_generator()
x[0][0] += r_1
x[0][1] += r_2
x[0][2] += r_3
for k in range(maxIter-1):

    timerInit = time()
    
    a = []
    for i in range(n):
        a.append(rho*(avg[k]-u[k][i])/(2*q[i] + rho)) 
    x.append(a)
    save_x = [private_key.decrypt(x) for x in x[k+1]]   # save for printing

    # Trusted party
    avg[k+1] = sum(x[k+1])/len(x[k+1])
    
    # update to parties
    b = []
    for i in range(n):        
        b.append(u[k][i] + x[k+1][i]-avg[k+1])
    u.append(b) 

    timer[0,k] = timerInit-time()
    
    plt.figure()
    plt.title('State Evolution')
    plt.xlabel('time')
    plt.ylabel('state')
    print_x.append(save_x)                              # Print_vector
    agent_1.append(print_x[k+1][0])
    agent_2.append(print_x[k+1][1])
    agent_3.append(print_x[k+1][2])
    
    t.append(k+1)
    plt.plot(t, agent_1, t, agent_2, t, agent_3)
    plt.axis([0, 17, 0, 1])


avg = [private_key.decrypt(x) for x in avg]


plt.figure()
plt.title('State Evolution')
plt.xlabel('time')
plt.ylabel('state')
plt.plot(t, agent_1, t, agent_2, t, agent_3, t, avg)
plt.axis([0, 17, 0, 1])
plt.savefig('OT.png')

plt.figure()
plt.title('Iteration Speed')
plt.xlabel('Iteration')
plt.ylabel('Duration [microseconds]')
plt.plot(t,-1E6*timer[0,:])
plt.savefig('OT_Timer.png')