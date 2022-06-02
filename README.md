To run last file below this github repository should be downloaded https://github.com/wbernoudy/ot.py

# Paillier & OT Encrypted ADMM Consensus
Firstly, in **plain.py** the ADMM concensus algorithm is implemented without any form of encryption.

Then, in **paillier.py**, the global variables are encrypted and are decrypted when consensus is reached

Lastly, in **ot.py**, a random number generator with oblivious transfer is used to conceal the initial values of the agents. These are used to solve the distributed consensus problem. For the random number generator, an additional script **random_number_generator.py** is written which makes use of the following github repository: https://github.com/wbernoudy/ot.py
