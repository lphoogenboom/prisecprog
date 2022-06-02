from time import time
import numpy as np
import matplotlib.pyplot as plt
from phe import paillier

maxIter = 18
n = 3
rho = 1
public_key, private_key = paillier.generate_paillier_keypair()
timer = []
t = [0]
#x = np.zeros([n,maxIter])
x = []
u = []
print_x = []
q = np.ones((n))

avg = np.zeros([1,maxIter]) 

# trusted party generates encryption for all avgs (operations can be done on encrypted data)
avg = [[public_key.encrypt(float(x)) for x in y] for y in avg][0] # Global variable must be encrypted

# agents send their initial state
xInit = [1, .3, .1] # initial state
xInit = [public_key.encrypt(float(i)) for i in xInit] # encrypt xInit
x.append(xInit) # trusted party stores x in encrypted form
print_x.append([1, .3, .1])
u.append([-1, -.3, .1])

plt.figure()

xEnc = []
k=0
concensus = 0
while (k<maxIter) and (concensus<3):
# for k in range(maxIter-1):
    print("iteration: ", k)
    timerInit = time() # init interation timer
    
    a = [] # tmp list for making 3x1 dim of x
    for i in range(n):
        a.append(rho*(avg[k]-u[k][i])/(2*q[i] + rho)) #state update of x
    x.append(a) # append 3xk to 3x(k+1) (encrypted)

    # print_x.append(save_x)
    avg[k+1] = sum(x[k+1])/len(x[k+1])

    b = []
    # update to parties
    for i in range(n):        
        b.append(u[k][i] + x[k+1][i]-avg[k+1])
    u.append(b) 
    timer.append(time()-timerInit)

    concensus = 0
    for i in range(n):
        if abs(private_key.decrypt(x[-1][i]-avg[k+1]))<.001:
            concensus+=1
    if concensus==n:
        print("concensus was acchieved at iteration: ", k)

    xDec = [[private_key.decrypt(i) for i in j] for j in x]
    agent_1 = []
    agent_2 = []
    agent_3 = []
    for i in range(len(xDec)):
        agent_1.append(xDec[i][0])
        agent_2.append(xDec[i][1])
        agent_3.append(xDec[i][2])
    xDec = []
    avgDec = []

    if (k>0):
        ax.clear()
    t.append(k+1)
    ax = plt.plot(t,agent_1,t,agent_2,t,agent_3)
    # plt.show() uncomment this line to show plot at every iterate
    k+=1







avg = [private_key.decrypt(y) for y in avg[0:k]]
plt.plot(t[0:-1],avg) 
plt.legend(["agent1","agent2","agent3","average"])
plt.savefig('Paillier.png')

plt.figure()
plt.title('Iteration Speed')
plt.xlabel('Iteration')
plt.ylabel('Duration [microseconds]')
plt.plot(t[1:],timer)
plt.savefig('PailierTimer.png')