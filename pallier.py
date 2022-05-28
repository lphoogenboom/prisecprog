from time import time
import numpy as np
import matplotlib.pyplot as plt
from phe import paillier

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


for k in range(maxIter-1):
    print("iteration: ", k)
    timerInit = time()
    
    a = []
    
    for i in range(n):
        a.append(rho*(avg[k]-u[k][i])/(2*q[i] + rho)) 
    
    x.append(a)
    
    # Trusted party
    save_x = [private_key.decrypt(x) for x in x[k+1]]
    print_x.append(save_x)
    avg[k+1] = sum(x[k+1])/len(x[k+1])
    
    b = []
    # update to parties
    for i in range(n):        
        b.append(u[k][i] + x[k+1][i]-avg[k+1])
    u.append(b) 

    timer[0,k] = timerInit-time()


avg = [private_key.decrypt(x) for x in avg]
t = np.linspace(0,17,18)

plt.figure()
plt.title('State Evolution')
plt.xlabel('time')
plt.ylabel('state')
agent_1 = []
agent_2 = []
agent_3 = []
for i in range(len(print_x)):
    agent_1.append(print_x[i][0])
    agent_2.append(print_x[i][1])
    agent_3.append(print_x[i][2])
    
plt.plot(t, agent_1, t, agent_2, t, agent_3, t, avg)
plt.axis([0, 17, 0, 1])
plt.savefig('Paillier.png')

plt.figure()
plt.title('Iteration Speed')
plt.xlabel('Iteration')
plt.ylabel('Duration [microseconds]')
plt.plot(t,-1E6*timer[0,:])
plt.axis([0, 16, 0, 60])
plt.savefig('PailierTimer.png')