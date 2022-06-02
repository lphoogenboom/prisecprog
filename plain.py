from time import time
import numpy as np
import matplotlib.pyplot as plt

maxIter = 18
n = 3
rho = 1

timer = np.zeros([1,maxIter])
x = np.zeros([n,maxIter])
q = np.ones([n, 1])
u = np.zeros([n,maxIter])
avg = np.zeros([maxIter])

x[:,0] = np.array([1, .3, .1])
u = -x

for k in range(maxIter-1):
    timerInit = time()
    for i in range(n):
        x[i,k+1] = rho*(avg[k]-u[i,k])/(2*q[i] + rho)

    avg[k+1] = np.mean(x[:,k+1])

    for i in range(n):
        u[i,k+1] = u[i,k]+x[i,k+1]-avg[k+1]
    timer[0,k] = timerInit-time()

t = np.linspace(0,17,18)

plt.figure()
plt.title('State Evolution')
plt.xlabel('time')
plt.ylabel('state')
plt.plot(t,x[0,:],t,x[1,:],t,x[2,:],t,avg)
plt.axis([0, 17, 0, 1])
plt.legend(["agent1","agent2","agent3","average"])
plt.savefig('plainX.png')

plt.figure()
plt.title('Iteration Speed')
plt.xlabel('Iteration')
plt.ylabel('Duration [milliseconds]')
plt.plot(t,-1E3*timer[0,:])
plt.savefig('plainTimer.png')