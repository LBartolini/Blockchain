from block import *
from blockchain import *
from user import *



u = User()
u.create_wallet()


'''
bc = Blockchain(5)
for n in range(10):
    bc.mine(Block("Block "+str(n+1)))

bc.printAll()
'''