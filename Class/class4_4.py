from mcpi.minecraft import Minecraft as mcs
from time import sleep
mc = mcs.create()
while True:
    sleep(0.5)
    mc.executeCommand("time add 200")