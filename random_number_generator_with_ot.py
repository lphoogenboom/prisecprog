#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:50:37 2022

@author: floriskrijgsman
"""

from ot import Alice, Bob

def random_number_generator():
    secrets = [b'-5', b'2.', b'3.']
    
    alice = Alice(secrets, 1, len(secrets[0]))
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
    return r_1, r_2, r_3
