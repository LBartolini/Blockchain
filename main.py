from block import *
from blockchain import *

bc = Blockchain(20)
for n in range(10):
    bc.mine(Block("Block "+str(n+1)))

bc.printAll()