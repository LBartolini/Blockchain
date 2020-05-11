from block import *
from blockchain import *
from user import *
from transaction import *


u = User()
u.create_wallet()

bc = Blockchain(5)
for n in range(10):
    bl = Block()
    tr = Transaction(u, {u.getPBL(): 4})
    tr.sign(u.private_key)
    bl.add_transaction(tr)
    bc.mine(bl)

bc.printAll()
