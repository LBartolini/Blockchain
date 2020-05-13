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
bc.addMoney(john.getPBL(), 100)
bc.addMoney(peter.getPBL(), 100)
bc.addMoney(ben.getPBL(), 100)



tr = Transaction(tom, {ben.getPBL(): 25}, bc)
bc.addTransaction(tr)
tr = Transaction(john, {peter.getPBL(): 75}, bc)
bc.addTransaction(tr)

tr = Transaction(ben, {tom.getPBL(): 5, john.getPBL(): 10}, bc)
bc.addTransaction(tr)

bc.mine()
bc.mine()


bc.printTail()

print("\n\n")
for us in users:
    print(us.username, ": ", bc.getBalance(us.getPBL()))
print(f"SUM: ", sum([bc.getBalance(i.getPBL()) for i in users]))