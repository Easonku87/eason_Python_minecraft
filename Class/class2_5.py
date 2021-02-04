from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
import time
while True:
    time.sleep(0.01)
    x,y,z=mc.player.getPos()
    a=mc.getBlock(x+1,y-1,z)
    b=mc.getBlock(x+1,y-1,z)
    c=mc.getBlock(x+1,y-1,z)
    d=mc.getBlock(x+1,y-1,z)
    if a==8 or b==8 or c==8 or d==8 or a==9  or b==9 or c==9  or d==9:
        mc.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,20)