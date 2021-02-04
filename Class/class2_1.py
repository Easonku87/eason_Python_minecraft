from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z=mc.player.getTilePos()
h=100
w=100
mc.setBlocks(x,y,z,x+w,y+h,z+w,41)
mc.setBlocks(x+w-1,y+h-1,z+w-1,x+1,y+1,z+1,0)