from time import time
import numpy as np
import matplotlib.pyplot as plt
from phe import paillier

maxIter = 18
n = 3
rho = 1
public_key, private_key = paillier.generate_paillier_keypair()
timer = np.zeros([1,maxIter])
x = np.zeros([n,maxIter])
print_x = np.zeros([n,maxIter])
q = np.ones([n, 1])
u = np.zeros([n,maxIter])
avg = np.zeros([1,maxIter]) 
h = np.float16(avg)
avg = [[public_key.encrypt(float(x)) for x in y] for y in avg] # Global variable must be encrypted

x[:,0] = np.array([1, .3, .1])
print_x[:,0] = x[:,0]
u = -x


for k in range(maxIter-1):
    timerInit = time()
    
    for i in range(n):
        x[i,k+1] = rho*(avg[0,k]-u[i,k])/(2*q[i] + rho)
    x[:, k+1] = [private_key.decrypt(x) for x in x[:,k+1]]
    print_x[:, k+1] = x[:, k+1]
    avg[:,k+1] = np.mean(x[:,k+1]) # Waarom is dit geen som? dat staat nmlk in de tekst
    avg = [[public_key.encrypt(float(x)) for x in y] for y in avg]
    for i in range(n):
        u[i,k+1] = u[i,k]+x[i,k+1]-avg[0,k+1]
    timer[0,k] = timerInit-time()
avg[0,0] = np.mean(x[:,0])


t = np.linspace(0,17,18)

plt.figure()
plt.title('State Evolution')
plt.xlabel('time')
plt.ylabel('state')
plt.plot(t,x[0,:],t,x[1,:],t,x[2,:],t,avg[0,:])
plt.axis([0, 17, 0, 1])
plt.savefig('plainX.png')

plt.figure()
plt.title('Iteration Speed')
plt.xlabel('Iteration')
plt.ylabel('Duration [microseconds]')
plt.plot(t,-1E6*timer[0,:])
plt.axis([0, 16, 0, 60])
plt.savefig('plainTimer.png')