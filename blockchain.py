from block import *
from user import *
from transaction import *

class Blockchain:

    maxNonce = 2**32
    miner_prize = 100
    halving_block_period = 1000

    def __init__(self, diff):
        self.tail = Block(self)  # last block of the chain GENESIS
        self.head = self.tail  # first block of the chain

        # WAITING BUFFERS
        self.blocks = []

        self.diff = diff
        self.target = 2 ** (256 - self.diff)

        self.admin = User() # admin RSA couple
        self.admin.create_wallet()

    def add(self, block):
        block.prev = self.tail
        block.bnumber = self.tail.bnumber + 1
        block.valid = True

        self.tail.next = block
        self.tail = self.tail.next

    def getBalance(self, public_key):
        # TODO: check balance from blocks that need to be inserted into the chain

        # checking blocks already inside the blockchain
        block = self.tail
        while block is not None:
            if True:  # TODO: call the check method of block to verify if everything is ok, in other words, check if this block is trustable
                for trans in block.transactions[::-1]:
                    if public_key in trans.balances:
                        return trans.balances[public_key]
                block = block.prev

        return 0

    def mine(self, miner, verbose=False):
        if len(self.blocks) > 0:
            block = self.blocks[0]
            block.signAll()

            if len(block.transactions) >= Block.min_transactions:
                for n in range(self.maxNonce):
                    if int(block.hash(), 16) <= self.target:
                        self.add(self.blocks.pop(0))
                        if verbose: print(block)
                        break
                    else:
                        block.nonce += 1

                self.addMoney(miner, self.miner_prize)

                if self.tail.bnumber % self.halving_block_period == 0:
                    self.miner_prize /= 2

    def addTransaction(self, transaction):
        if len(self.blocks) == 0:
            self.blocks.append(Block(self))
            self.blocks[-1].add_transaction(transaction)
        else:
            # there is at least one block waiting to be mined
            found_another = False
            for bl in self.blocks:
                found_another = False

                if len(bl.transactions) > bl.max_transactions:
                    continue

                for trans in bl.transactions:
                    for key in transaction.getWallets():
                        if key in trans.getWallets():
                            found_another = True

                if not found_another:
                    bl.add_transaction(transaction)
                    break

            if found_another:
                # every block has at least something to do with one or more wallets in this new transaction
                self.blocks.append(Block(self))
                self.blocks[-1].add_transaction(transaction)

    def addMoney(self, wallet, amount):
        tr = Transaction(self.admin, {wallet: amount}, self)
        self.addTransaction(tr)

    def printTail(self, number=50):
        tmp = self.tail
        i = number
        while tmp is not None and i > 0:
            print(tmp.print_values())
            tmp = tmp.prev
            i -= 1
