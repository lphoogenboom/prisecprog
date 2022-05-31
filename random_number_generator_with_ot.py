#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:50:37 2022

@author: floriskrijgsman
"""
# random number generator with OT scheme
# it is a bit far fetched but it does the job I guess


from random import seed
from random import random
from ot import Alice, Bob


secrets = [b'-5', b'2.', b'3.']

alice = Alice(secrets, 1, len(secrets[0]))
#agent_2 = Alice(secrets, 1, len(secrets[0]))
#agent_3 = Alice(secrets, 1, len(secrets[0]))
alice.setup()

agent_1 = Bob([0])
agent_2 = Bob([1])
agent_3 = Bob([2])
agent_1.setup()
alice.transmit()
a = agent_1.receive()
r_1 = float(a[0].decode("utf-8"))

agent_2.setup()
alice.transmit()
b = agent_2.receive()
r_2 = float(b[0].decode("utf-8"))

agent_3.setup()
alice.transmit()
c = agent_3.receive()
r_3 = float(c[0].decode("utf-8"))