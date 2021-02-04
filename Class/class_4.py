# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:23:13 2021

@author: USER
"""
from mcpi.minecraft import Minecraft as mcs
import time
mc = mcs.create()
t=0
while True:
    time.sleep(5)
    mc.postToChat('t='+str(t))
    t=t+1
                           