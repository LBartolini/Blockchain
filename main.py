from block import *
from blockchain import *
from user import *
from transaction import *


u = User()
u.create_wallet()

bc = Blockchain(10)
for n in range(10):
    bl = Block()
    tr = Transaction(u, u.public_key, 4)
    tr.sign()
    bl.add_transaction(tr)
    bc.mine(bl)

bc.printAll()
