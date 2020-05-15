from block import *
from blockchain import *
from user import *
from transaction import *



tom = User("Tom")
tom.create_wallet()

ben = User("Ben")
ben.create_wallet()

john = User("John")
john.create_wallet()

peter = User("Peter")
peter.create_wallet()

users = [tom, ben, john, peter]

bc = Blockchain(5)
bc.addMoney(tom.getPBL(), 100)

tr = Transaction(tom, {ben.getPBL(): 50}, bc)
bc.addTransaction(tr)

bc.mine(ben.getPBL())

bc.printTail()

print("\n\n")
for us in users:
    print(us.username, ": ", bc.getBalance(us.getPBL(), True))
print(f"SUM: ", sum([bc.getBalance(i.getPBL(), True) for i in users]))