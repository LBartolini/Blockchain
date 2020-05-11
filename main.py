from block import *
from blockchain import *
from user import *
from transaction import *


u = User()
u.create_wallet()

admin = User()
admin.create_wallet()

bc = Blockchain(5, admin.getPBL())

bl = Block(bc)
tr = Transaction(admin, {u.getPBL(): 100}, bl)
tr.sign()
bl.add_transaction(tr)
bc.mine(bl)

for n in range(10):
    bl = Block(bc)
    tr = Transaction(u, {u.getPBL(): 4}, bl)
    tr.sign()
    bl.add_transaction(tr)
    bc.mine(bl)

bc.printTail(5)