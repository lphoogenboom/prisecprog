# Paillier & OT Encrypted ADMM Consensus
## Plain
Firstly, in **plain.py** the ADMM concensus algorithm is implemented without any form of encryption.

## Paillier
Then, in **paillier.py**, the global variables are encrypted and are decrypted when consensus is reached
The **Paillier.py** file depends on the phe.paillier library, which can be installed using pip or conda

## Paillier with oblivious transfer
Lastly, in **ot.py**, a random number generator with oblivious transfer is used to conceal the initial values of the agents. These are used to solve the distributed consensus problem. For the random number generator, an additional script **random_number_generator.py** is written which makes use of the following github repository: https://github.com/wbernoudy/ot.py
