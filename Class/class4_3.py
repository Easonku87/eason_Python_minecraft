from mcpi.minecraft import Minecraft as mcs
import random
mc = mcs.create()
x,y,z = mc.player.getPos()
Blen = 4
for i in range(4):
   for i in range(4):
      num = random.randint(1,4)
      if num == 1:
          mc.setBlocks(x,y,z,x+Blen,y,z)
          x = x + Blen
      elif num == 2:
          mc.setBlocks(x,y,z,x-Blen,y,z+1)
          x = x + Blen   
      else:
          mc.setBlocks(x,y,z,x,y,z-Blen,1)
          z = z - Blen